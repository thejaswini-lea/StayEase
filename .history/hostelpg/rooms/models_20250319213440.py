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

from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Available")
    def __str__(self):
        return f"Room {self.number} ({self.room_type})"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking for {self.room.number} by {self.name}"


class Review(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"
