from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view(), name='restaurants'),
    path('hotels/', views.HotelList.as_view(), name='hotels'),
    path('lodges/', views.LodgeList.as_view(), name='lodges'),
    path('resorts/', views.ResortList.as_view(), name='resorts')
]
