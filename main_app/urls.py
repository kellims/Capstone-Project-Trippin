from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('trips/', views.TripList.as_view(), name="trip_list"),
    path('trips/new/', views.TripCreate.as_view(), name="trip_create"),
    path('trips/<int:pk>/', views.TripDetail.as_view(), name="trip_detail"),
    path('trips/<int:pk>/update',views.TripUpdate.as_view(), name="trip_update"),
]