# library_management/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # books
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # members
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.member_create, name='member_create'),

    # borrow
    path('borrow/', views.borrow_create, name='borrow_create'),
    path('borrow/<int:pk>/return/', views.borrow_return, name='borrow_return'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
