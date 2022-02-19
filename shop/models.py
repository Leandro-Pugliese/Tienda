
from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("nombre",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('shop : Producto_por_Categoria', args=[self.slug])




class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to="productos/%Y/%m/%d", blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    class Meta:
        ordering = ("nombre",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("shop : Detalle_Producto", args=[self.id, self.slug])

