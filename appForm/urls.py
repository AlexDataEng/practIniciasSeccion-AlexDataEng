from django.urls import path
from .views import home,  formulario_cliente

urlpatterns = [
    path("", home),
    path('formulario/', formulario_cliente, name='formulario_cliente')
]
