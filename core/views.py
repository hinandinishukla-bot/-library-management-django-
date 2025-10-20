# core/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db import transaction
from .models import Book, Loan, Reservation
from .serializers import BookSerializer, LoanSerializer, ReservationSerializer
from .permissions import IsLibrarianOrReadOnly
from datetime import timedelta

LOAN_DAYS = 14  # default loan period

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    permission_classes = [IsLibrarianOrReadOnly]

    @action(detail=True, methods=["post"], url_path="adjust-copies", permission_classes=[IsLibrarianOrReadOnly])
    def adjust_copies(self, request, pk=None):
        book = self.get_object()
        delta = int(request.data.get("delta", 0))
        if delta == 0:
            return Response({"detail":"No change"}, status=400)
        book.total_copies = max(0, book.total_copies + delta)
        book.available_copies = max(0, book.available_copies + delta)
        book.save()
        return Response(BookSerializer(book).data)

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.select_related("user","book").all().order_by("-borrowed_at")
    serializer_class = LoanSerializer

    def get_permissions(self):
        # allow create via authenticated users; return actions allowed for all authenticated
        return []

    def create(self, request, *args, **kwargs):
        # Borrow flow: expect user_id & book_id in payload
        user_id = request.data.get("user_id")
        book_id = request.data.get("book_id")
        if not user_id or not book_id:
            return Response({"detail":"user_id and book_id required"}, status=400)

        with transaction.atomic():
            try:
                book = Book.objects.select_for_update().get(id=book_id)
            except Book.DoesNotExist:
                return Response({"detail":"Book not found"}, status=404)

            if book.available_copies <= 0:
                return Response({"detail":"No copies available"}, status=400)

            book.available_copies -= 1
            book.save()

            due_date = timezone.now() + timedelta(days=LOAN_DAYS)
            loan = Loan.objects.create(user_id=user_id, book_id=book_id, due_date=due_date)
            serializer = LoanSerializer(loan)
            return Response(serializer.data, status=201)

    @action(detail=True, methods=["post"], url_path="return")
    def return_book(self, request, pk=None):
        with transaction.atomic():
            try:
                loan = Loan.objects.select_for_update().get(id=pk)
            except Loan.DoesNotExist:
                return Response({"detail":"Loan not found"}, status=404)
            if loan.returned_at:
                return Response({"detail":"Already returned"}, status=400)

            loan.returned_at = timezone.now()
            if loan.returned_at > loan.due_date:
                days_late = (loan.returned_at - loan.due_date).days
                loan.fine_amount = days_late * 1.00  # ₹1 per day example
                loan.status = "returned"
            else:
                loan.status = "returned"
            loan.save()

            # increment book copies
            book = Book.objects.select_for_update().get(id=loan.book_id)
            book.available_copies += 1
            book.save()

            return Response(LoanSerializer(loan).data)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by("-created_at")
    serializer_class = ReservationSerializer
