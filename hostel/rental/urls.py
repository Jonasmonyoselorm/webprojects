from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_us, name='contactUs'),
]