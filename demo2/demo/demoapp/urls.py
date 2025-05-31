from django.urls import path
from . import views

urlpatterns = [
    path('',  views.HolaMundo),
    path ('about/', views.About),
    path ('jolines/', views.Jolines),
    path ('pito/', views.Pito),
]