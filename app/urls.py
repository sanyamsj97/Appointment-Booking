
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    path('client/', include("client.urls")),
    path('server/', include("server.urls")),
]
