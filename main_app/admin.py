from django.contrib import admin
from .models import Trip, Reservation

# Register your models here.

admin.site.register(Trip)
admin.site.register(Reservation)