from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('videojuegos', views.videojuegos, name='videojuegos'),
    path('maquetas', views.maquetas, name='maquetas'),
    path('cartasycoleccionables', views.cartasycoleccionables, name='cartasycoleccionables'),
    path('entrar', views.entrar, name='entrar'),
    path('registrar', views.registrar, name='registrar'),
    path('pagconstruccion', views.pagconstruccion, name='pagconstruccion'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name="registro")
]