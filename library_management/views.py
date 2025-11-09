# library_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Book, Member, Borrow
from .forms import BookForm, MemberForm, BorrowForm
from django.utils import timezone
from datetime import timedelta

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid credentials or not an admin"
    return render(request, 'login.html', {'error': error})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    total_books = Book.objects.count()
    available_books = Book.objects.filter(available_copies__gt=0).count()
    total_members = Member.objects.count()
    total_borrows = Borrow.objects.count()
    active_borrows = Borrow.objects.filter(returned=False).count()
    overdue_borrows = sum(1 for b in Borrow.objects.filter(returned=False) if b.is_overdue())

    # top borrowed books
    top_books = Book.objects.annotate(bcount=Count('borrows')).order_by('-bcount')[:5]
    chart_labels = [b.title for b in top_books]
    chart_data = [b.bcount for b in top_books]

    recent_books = Book.objects.order_by('-created_at')[:8]
    context = {
        'total_books': total_books,
        'available_books': available_books,
        'total_members': total_members,
        'total_borrows': total_borrows,
        'active_borrows': active_borrows,
        'overdue_borrows': overdue_borrows,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'recent_books': recent_books,
    }
    return render(request, 'dashboard.html', context)

# Book views
@login_required
def book_list(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'books': books})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'book': book})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# Member views
@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

@login_required
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

# Borrow views
@login_required
def borrow_create(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            # adjust available copies
            if borrow.book.available_copies > 0:
                borrow.book.available_copies -= 1
                borrow.book.save()
                borrow.save()
                return redirect('dashboard')
            else:
                form.add_error('book', 'Book not available')
    else:
        form = BorrowForm(initial={'issue_date': timezone.now().date(), 'due_date': timezone.now().date() + timedelta(days=14)})
    return render(request, 'borrow_form.html', {'form': form})

@login_required
def borrow_return(request, pk):
    b = get_object_or_404(Borrow, pk=pk)
    if not b.returned:
        b.returned = True
        b.return_date = timezone.now().date()
        b.save()
        b.book.available_copies += 1
        b.book.save()
    return redirect('dashboard')
