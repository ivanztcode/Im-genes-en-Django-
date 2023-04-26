from django.db import models
from django.utils.html import format_html

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Producto" , max_length=50)
    descripcion = models.TextField(verbose_name="Descripción del producto")
    precio = models.DecimalField(verbose_name="Precio del producto" ,max_digits=7, decimal_places=2)
    cantidad = models.IntegerField(verbose_name="Stock")
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField("Imagen del Producto",upload_to="productos/",null=True, blank=True)

    class Meta:
        ordering =["nombre"]
        
    def __str__(self):
        return self.nombre
    
    def imagen_reducida(self):
        if self.imagen:
            return format_html('<img src="{}" width="100" height="100" />'.format(self.imagen.url))
        else:
            return ''
    imagen_reducida.short_description = 'Imagen'