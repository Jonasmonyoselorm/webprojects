from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_us, name='contactUs'),
    path('about/', views.about_us, name='aboutUs'),
    path('four-in-one/', views.four_in_one, name='four-in-one'),
    path('three-in-one/', views.three_in_one, name='three-in-one'),
]


