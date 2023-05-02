from .models import productos, Categoriaproductos
from rest_framework import serializers



class CategoriaproductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoriaproductos
        fields = '__all__'
    


class productosSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="Categoria.nombrecate")
    class Meta:
        model = productos
        fields = '__all__' 