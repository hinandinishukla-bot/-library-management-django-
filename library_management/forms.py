# library_management/forms.py
from django import forms
from .models import Book, Member, Borrow
from django.utils import timezone

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'total_copies', 'available_copies', 'cover']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['member', 'book', 'issue_date', 'due_date']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type':'date'}),
            'due_date': forms.DateInput(attrs={'type':'date'}),
        }
