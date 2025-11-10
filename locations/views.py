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
    