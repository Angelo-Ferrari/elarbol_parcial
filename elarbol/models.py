from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Producto(models.Model):


    nombre_producto           = models.CharField(max_length=50, blank=False, null=False, unique=True)
    precio           = models.IntegerField(blank=False, null=False)
    stock           = models.IntegerField(blank=False, null=False)
    descripcion              = models.CharField(max_length=200)
    activo           = models.IntegerField(blank=False, null=False)
    foto_producto          = models.ImageField(blank=True, null=True)


    class Meta:
        ordering = ['nombre_producto']


    def __str__(self):
        return f' item: {self.nombre_producto}'
