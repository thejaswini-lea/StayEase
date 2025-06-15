from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Under Maintenance', 'Under Maintenance')
    ]
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.number} - {self.room_type}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking for {self.room.number} by {self.name}"
