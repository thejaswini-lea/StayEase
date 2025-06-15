from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking
from .forms import RoomForm, BookingForm

def home(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/home.html', {'rooms': rooms})

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'rooms/add_room.html', {'form': form})

from django.contrib import messages

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was successful!")
            return redirect('booking_success')  # Redirect to success page
    else:
        form = BookingForm(initial={'room': room})
    return render(request, 'rooms/book_room.html', {'form': form, 'room': room})
