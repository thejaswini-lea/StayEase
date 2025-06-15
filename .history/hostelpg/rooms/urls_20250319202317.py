from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-room/', views.add_room, name='add_room'),
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('booking-success/', views.booking_success, name='booking_success'),
]
