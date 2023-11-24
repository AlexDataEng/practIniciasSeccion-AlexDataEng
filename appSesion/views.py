from django.shortcuts import render, redirect
from .models import Sesion

# Create your views here.
def home(requests):
    return render(requests, "login.html")

def iniciarSesion(request):
    
    nombre = request.POST.get("nombre")

    if nombre:
        # Obtener un conjunto de objetos que coincidan con el nombre
        sesiones = Sesion.objects.filter(nombres=nombre)

        if sesiones.exists():  # Verifica si hay sesiones que coincidan con el nombre
            primera_sesion = sesiones.first()  # Tomamos la primera sesión (puedes ajustar esto según tus necesidades)

            # Obtén la contraseña de la sesión
            contrasena = primera_sesion.contrasena
            
            # Haces algo con la contraseña, por ejemplo, imprimir
            print(f"Contraseña encontrada para {nombre}: {contrasena}")

        else:
            print(f"No se encontró ninguna sesión para el nombre: {nombre}")
    else:
        print("El nombre no fue proporcionado en la solicitud POST")
    return render(request, "login.html")