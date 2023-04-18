from django.db import models

# Create your models here.#

class Categoriaproductos(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombrecate = models.CharField(max_length=30, null=False, verbose_name='nombre')

    def __str__(self):
        return self.nombrecate

class productos(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=5)
    Nombre = models.CharField(max_length=40)
    Descripcion = models.TextField()
    Cantidad= models.IntegerField()
    Precio= models.IntegerField()
    Categoria = models.ForeignKey(Categoriaproductos, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre
    
