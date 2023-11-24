from django.shortcuts import render, redirect
from .models import Usuario, Productos

# Create your views here.
def home(requests):
    return render(requests, "formulario-clientes.html")


#Insertar cliente + producto
def formulario_cliente(request):
    if request.method == 'POST':
        # Obtener los datos del formulario

        rut = request.POST.get('rut')
        nombres = request.POST.get('nombres')
        tipo_usuario = request.POST.get('tipoUsuario')
        contrasena = request.POST.get('contrasena')

        codigo = request.POST.get('codigo')
        lote = request.POST.get('lote')
        producto = request.POST.get('producto')
        totalFacturado = request.POST.get('totalFacturado')
        totalDevuelto = request.POST.get('totalDevuelto')

        # Crear un objeto Usuario y guardarlo en la base de datos
        usuario = Usuario.objects.create(
            rut=rut,
            nombres=nombres,
            tipoUsuario=tipo_usuario,
            contrasena=contrasena
        )
        usuario.save()

        producto = Productos(
            codigo = codigo,
            lote = lote,
            producto = producto,
            totalFacturado = totalFacturado,
            totalDevuelto = totalDevuelto
        )

        producto.save()

        # Crear 

        # Redireccionar a la página de éxito o a donde desees
        return redirect("login.html")

    # Si el método no es POST, renderiza el formulario
    return render(request, "formulario-clientes.html")
    

