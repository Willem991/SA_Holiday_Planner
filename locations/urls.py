from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view(), name='restaurants')
]
