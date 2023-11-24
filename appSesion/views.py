from django.shortcuts import render, redirect
from .models import Sesion
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Decorador para autentificacion
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):

    """ if request.method == 'POST':
        # Lógica de autenticación aquí
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Después de autenticar al usuario, redirige a la URL original o a una predeterminada.
            next_url = request.GET.get('next', '/sesion/inicio-informe/')
            return redirect(next_url)"""

    return render(request, './registration/login.html')




def logout_view(request):
    logout(request)
    # Redirige a la URL configurada en LOGOUT_URL o a la que desees.
    return redirect('./registration/cerrar_sesion.html')






# Landing Page
def homeInforme(request):
    return render(request, "inicio-informe.html")

# Pagina Incio
def home(request):
    return render(request, "inicio.html")



"""
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
            return redirect("inicio.html")
        else:
            print(f"No se encontró ninguna sesión para el nombre: {nombre}")
    else:
        print("El nombre no fue proporcionado en la solicitud POST")
    return render(request, "login.html")
"""