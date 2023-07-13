from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse

from .models import Trip

# Create your views here.



class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html" 


class TripList(TemplateView):
    template_name = "trip_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trips"] = Trip.objects.all()
        return context
    
class TripCreate(CreateView):
    model = Trip
    fields = ['location', 'description', 'start_date', 'end_date', 'image']
    template_name = "trip_create.html"
    
    def get_success_url(self):
        return reverse('trip_detail', kwargs={'pk': self.object.pk})


class TripDetail(DetailView):
    model = Trip
    template_name = "trip_detail.html"


class TripUpdate(UpdateView):
    model = Trip
    fields = ['location', 'description', 'start_date', 'end_date', 'image']
    template_name = "trip_update.html"
    
    def get_success_url(self):
        return reverse('trip_detail', kwargs={'pk': self.object.pk})