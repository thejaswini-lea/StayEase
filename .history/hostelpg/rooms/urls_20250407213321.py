from django.urls import path
from . import views
from .views import room_detail
from .views import signup_view, login_view, logout_view
urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),  # ✅ Edit Room URL
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),  # ✅ Delete Room URL
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),
    path('signup/', signup_view, name='signup'),
    path('login/', name='login'),
    path('logout/', logout_view, name='logout'),
]

