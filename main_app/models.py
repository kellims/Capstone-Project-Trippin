from django.db import models

# Create your models here.

class Trip(models.Model):

    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.CharField(max_length=20000, default='default_image.html')
    
    def __str__(self):
        return self.location

    class Meta:
        ordering = ['start_date']