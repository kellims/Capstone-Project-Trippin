from django.db import models

# Create your models here.

class Trip(models.Model):

    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    reservation = models.URLField(max_length=1000, blank=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date']