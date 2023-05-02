from django.urls import path, include
from . import views
from.views import productosViewset, CategoriaproductosViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('productos', productosViewset)
router.register('Categoriaproductos', CategoriaproductosViewset)


urlpatterns = [
    path('', views.index, name='index'),
    path('videojuegos', views.videojuegos, name='videojuegos'),
    path('maquetas', views.maquetas, name='maquetas'),
    path('cartasycoleccionables', views.cartasycoleccionables, name='cartasycoleccionables'),
    path('entrar', views.entrar, name='entrar'),
    path('registrar', views.registrar, name='registrar'),
    path('pagconstruccion', views.pagconstruccion, name='pagconstruccion'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name="registro"),
    path('api/', include(router.urls)),
]