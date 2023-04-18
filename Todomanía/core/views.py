from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import productos
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    producto = productos.objects.all()
    data ={
        'producto' : producto
        }
    return render(request, 'core/index.html', data)

def videojuegos(request):
    producto = productos.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'core/Videojuegos.html', data)

def maquetas(request):
    return render(request, 'core/Maquetas.html')

def cartasycoleccionables(request):
    return render(request, 'core/cartas_coleccionables.html')

def entrar(request):
    return render(request, 'core/Entrar.html')

def registrar(request):
    return render(request, 'core/Registrar.html')

def pagconstruccion(request):
    return render(request, 'core/pagina_cons.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")      
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)






