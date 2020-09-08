from django.urls import path
from maturity_calculator import views

urlpatterns = [
    path('', views.calculate, name = 'calculate'),
]