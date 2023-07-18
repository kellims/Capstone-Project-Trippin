from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):

    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.CharField(max_length=20000, default='default_image.html')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.location

    class Meta:
        ordering = ['start_date']




class Reservation(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=150)
    file = models.URLField(max_length=1000, blank=True)

    # Reviewed documention on how to add choices. Trying to add choices below:
    DINING = 'Dining'
    HOTEL = 'Hotel'
    TRANSPORTATION = 'Transportation'
    DAY_TRIP = 'Day Trip'
    MUSEUM = 'Museum'
    SITE_SEEING = 'Site Seeing'
    TOUR = 'Tour'
    OTHER = 'Other'

    type_choices = [
        (DINING, "Dining"),
        (HOTEL, "Hotel"),
        (TRANSPORTATION, "Transportation"),
        (DAY_TRIP, "Day Trip"),
        (MUSEUM, "Museum"),
        (SITE_SEEING, "Site Seeing"),
        (TOUR, "Tour"),
        (OTHER, "Other"),
    ]
    type = models.CharField(choices=type_choices, max_length=150)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="reservations")

    def __str__(self):
        return self.name        
    
    class Meta:
        ordering = ['start_date']