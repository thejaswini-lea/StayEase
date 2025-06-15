from django import forms
from .models import Room, Booking

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'name', 'email', 'phone', 'check_in', 'check_out']

