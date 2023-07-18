from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    # path('', include('main_app.urls')),
    path('', views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('about/', views.About.as_view(), name="about"),
    path('trips/', views.TripList.as_view(), name="trip_list"),
    path('trips/new/', views.TripCreate.as_view(), name="trip_create"),
    path('trips/<int:pk>/', views.TripDetail.as_view(), name="trip_detail"),
    path('trips/<int:pk>/update',views.TripUpdate.as_view(), name="trip_update"),
    path('trips/<int:pk>/delete',views.TripDelete.as_view(), name="trip_delete"),
    path('trips/<int:pk>/reservations/new/', views.ReservationCreate.as_view(), name="reservation_create"),
    path('trips/<int:pk>/reservations/', views.ReservationDetail.as_view(), name="reservation_detail"),
    path('trips/<int:pk>/reservations/update', views.ReservationUpdate.as_view(), name="reservation_update"),
    path('trips/<int:pk>/reservations/delete', views.ReservationDelete.as_view(), name="reservation_delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]