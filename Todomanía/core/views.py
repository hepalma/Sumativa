from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def videojuegos(request):
    return render(request, 'core/Videojuegos.html')
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



