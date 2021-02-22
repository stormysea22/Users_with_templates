from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('employee/new', views.new_employee),
    path('employee/create', views.create_employee),
]