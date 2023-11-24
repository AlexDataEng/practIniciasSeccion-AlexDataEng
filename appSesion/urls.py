from django.urls import path
from .views import home, iniciarSesion

urlpatterns = [
    path("", home),
    path("iniciar/", iniciarSesion, name="iniciarSesion"),
    
]
