# Django-appointment-and-booking-system
A  python prototype Django project for booking and appoientment for server and client

#This  web application has several important features :
(i) Easy appointment creation  for server 
(ii) Easy date picker, time picker and auto time suggestion while creating new appointment
(ii) Appointment edit and deletion  option 
(iv) Success notification
(v) Search  option with numeric and string
(vi) Calendar Integration
(vii) Central administrator
(viii) Different type of profile group like server and client 
(ix) Modular Login system



Deployment in localhost windows pc:
####################################
To run this project in localhost , we have to setup python, pip, virtualenv and django.
Frist,  we have to make sure that we  have installed pip and python in our pc. Then,

1. Run Windows Powershell as Administrator

We have to create a new directory to install virtualenv . Browse that directory via command and run. separate virtual server for each project is best, it will not affect other project library.

2. pip install virtualenv
3. virtualenv .
4. Scripts\activate or scripts\activate

Now we have to create another directory inside virtualenv, then we have to install django inside it. Browse that new directory via command line and install django inside it.

5. pipenv install django /pip install django

Copy this  whole oproject inside django directory, browse the app and run 
python .\manage.py runserver

After successfully deployment we will  require this User access for the project: 
Supersuer: admin (url: http://127.0.0.1:8000/admin)
Other User: server1, server2, client1, client2 (url: http://127.0.0.1:8000/)
password for all admin and user: Saroar123

*Inside project some url is not dynamically set, I forget to do that

**See the screens.pdf for scrrenshot of the project
