from django.db import models

# Create your models here.
from core.models import Category


class Product(models.Model):
    name = models.CharField(verbose_name='Nombre del Producto', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descripcion del producto', max_length=500)
    foto = models.ImageField(verbose_name='Agregar imagen', null=True, upload_to='Inventario')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Nuevo Producto a Inventario'
        verbose_name_plural ='Nuevos Productos a Inventario'


class Inventario(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Seleccione el producto')
    fechaIngreso = models.DateTimeField(verbose_name='Fecha de ingreso')
    perecedero = models.BooleanField(verbose_name='¿Es Perecedero?', default=False)

    def __str__(self):
        return 'Producto {0}, se ingreso el {1}'.format(self.producto, self.fechaIngreso)

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'