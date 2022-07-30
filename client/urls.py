from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	client,
	quick_appointment,
	appointment_book,
	)

urlpatterns = [
    path('', views.client, name='client'),
    path('my_appointment/', views.client, name='client'),
    path('quick_appointment/', views.quick_appointment, name='quick_appointment'),   
    path('update/<int:id>/', views.appointment_book,name='appointment_update'),
      
]
