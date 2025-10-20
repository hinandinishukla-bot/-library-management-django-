# core/serializers.py
from rest_framework import serializers
from .models import Book, Loan, Reservation, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","first_name","last_name","role")

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ("available_copies","created_at")

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=True)
    book_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Loan
        fields = ("id","user","book","user_id","book_id","borrowed_at","due_date","returned_at","status","fine_amount")

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ("created_at",)
