# library_management/models.py
from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200, blank=True)
    isbn = models.CharField(max_length=50, blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    cover = models.ImageField(upload_to='books/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    join_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrows')
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    return_date = models.DateField(null=True, blank=True)

    def is_overdue(self):
        if self.returned:
            return False
        return timezone.now().date() > self.due_date

    def __str__(self):
        return f"{self.book.title} -> {self.member.name}"
