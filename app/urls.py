from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_video_view),
    path('salons/', views.salons_view),
    path('cosmetics/', views.cosmetics_view),
    path('event-hall/', views.event_hall_view),
    path('food-court/', views.food_court_view),
    path('designing-stitching/', views.designing_view),
    path('academy/', views.academy_view),
    path('franchise/', views.franchise_view),
    path('about-us/', views.about_us_view),
    path('contact/', views.contact_view),
]
