from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),  # ✅ Edit Room URL
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),  # ✅ Delete Room URL
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('booking-success/', views.booking_success, name='booking_success'),
]

