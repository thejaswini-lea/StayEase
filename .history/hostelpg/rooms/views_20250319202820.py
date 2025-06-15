from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking
from .forms import RoomForm, BookingForm

def home(request):
    return render(request, 'rooms/home.html')  # Only shows homepage

 # ✅ New page for rooms

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Redirect to new rooms page
    else:
        form = RoomForm()
    return render(request, 'rooms/add_room.html', {'form': form})

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was successful!")
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'room': room})
    return render(request, 'rooms/book_room.html', {'form': form, 'room': room})

def booking_success(request):
    return render(request, 'rooms/booking_success.html')
