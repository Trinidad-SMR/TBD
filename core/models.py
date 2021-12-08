from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


# Create your models here.
class Product(models.Model):
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Seleccione la categoria del producto')
    name = models.CharField(verbose_name='Producto', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descripcion del producto', max_length=500)
    price = models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2, default=0.00)
    foto = models.ImageField(verbose_name='Agregar imagen', null=True, upload_to='imgProducts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Proveedor(models.Model):
    name = models.CharField(verbose_name='Proveedor', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Marca(models.Model):
    name = models.CharField(verbose_name='Marca', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Venta(models.Model):
    name = models.CharField(verbose_name='Venta', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
