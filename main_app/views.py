from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect

from .models import Trip, Reservation

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


class TripDelete(DeleteView):
    model = Trip
    template_name = "trip_delete_confirmation.html"
    success_url = "/trips/"


class ReservationCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        location = request.POST.get("location")
        type = request.POST.get("type")
        file = request.POST.get("file")
        trip = Trip.objects.get(pk=pk)
        Reservation.objects.create(name=name, description=description, start_date=start_date, end_date=end_date, location=location, type=type, file=file, trip=trip)
        return redirect('trip_detail', pk=pk)
    


