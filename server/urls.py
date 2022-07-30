from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	server,
	server_appointment_list,
	appointment_delete,
	server_appointment_update,
	)





urlpatterns = [
    path('', views.server, name='server_home'),
    path('my_appointment/', views.server, name='server_appointment'),
    path('create_appointment/', views.server_appointment_list, name='server_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', server_appointment_update,name='server_appointment_update'),      
      
]

