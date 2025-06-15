from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking
from .forms import RoomForm, BookingForm

def home(request):
    return render(request, 'rooms/home.html')  # Only shows homepage

def room_list(request):
    rooms = Room.objects.all()
    
    for room in rooms:
        # Check if there's an active booking for this room
        is_booked = Booking.objects.filter(room=room).exists()
        if is_booked:
            room.status = "Occupied"
        else:
            room.status = "Available"

    return render(request, 'rooms/room_list.html', {'rooms': rooms})
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

def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Redirect back to room list
    else:
        form = RoomForm(instance=room)
    return render(request, 'rooms/edit_room.html', {'form': form, 'room': room})

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')  # Redirect back after deletion
    return render(request, 'rooms/delete_room.html', {'room': room})  # Confirmation page

