from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Accommodations
import os

# Create your views here.
class RestaurantList(ListView):
    model = Accommodations
    template_name = 'locations/restaurant_list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return super().get_queryset().filter(type='restaurant')
    
class HotelList(ListView):
    model = Accommodations
    template_name = 'locations/hotel_list.html'
    context_object_name = 'hotels'

    def get_queryset(self):
        return super().get_queryset().filter(type='hotel')
    
class ResortList(ListView):
    model = Accommodations
    template_name = 'locations/resort_list.html'
    context_object_name = 'resorts'

    def get_queryset(self):
        return super().get_queryset().filter(type='resort')
    
class LodgeList(ListView):
    model = Accommodations
    template_name = 'locations/lodge_list.html'
    context_object_name = 'lodges'

    def get_queryset(self):
        return super().get_queryset().filter(type='lodge')
    