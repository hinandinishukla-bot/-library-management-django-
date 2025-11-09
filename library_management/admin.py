# library_management/admin.py
from django.contrib import admin
from .models import Book, Member, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'total_copies', 'available_copies')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'join_date')
    search_fields = ('name', 'email')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'issue_date', 'due_date', 'returned', 'return_date')
    list_filter = ('returned',)
    search_fields = ('book__title', 'member__name')
