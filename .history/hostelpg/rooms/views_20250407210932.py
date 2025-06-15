from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking
from .forms import RoomForm, BookingForm

def convert_to_inr(price_in_usd):
    exchange_rate = 83  # Update this rate based on real-time value
    return price_in_usd * exchange_rate

def home(request):
    return render(request, 'rooms/home.html')  # Only shows homepage

def room_list(request):
    rooms = Room.objects.all()
    
    for room in rooms:
        # Convert price to INR before sending it to the template
        room.price_inr = convert_to_inr(room.price)

        # Check if there's an active booking for this room
        is_booked = Booking.objects.filter(room=room).exists()
        if is_booked:
            room.status = "Occupied"
        else:
            room.status = "Available"

    return render(request, 'rooms/room_list.html', {'rooms': rooms})

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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Review
from .forms import ReviewForm

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    reviews = room.reviews.all()  # Fetch all reviews for the room

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.room = room
            review.save()
            return redirect('room_detail', room_id=room.id)
    else:
        form = ReviewForm()

    return render(request, 'rooms/room_detail.html', {'room': room, 'reviews': reviews, 'form': form})

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
