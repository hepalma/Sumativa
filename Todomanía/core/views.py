from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import productos, Categoriaproductos
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import productosSerializer, CategoriaproductosSerializer

# Create your views here.
class CategoriaproductosViewset(viewsets.ModelViewSet):
    queryset = Categoriaproductos.objects.all()
    serializer_class = CategoriaproductosSerializer

class productosViewset(viewsets.ModelViewSet):
    queryset = productos.objects.all()
    serializer_class = productosSerializer

    def get_queryset(self):
        producto = productos.objects.all()

        nombre = self.request.GET.get('Nombre')
        if nombre:
            producto = producto.filter(nombre__contains=nombre)

        return producto  
     



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






