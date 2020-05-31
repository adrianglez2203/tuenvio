from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length=25)
    url_de_busqueda = models.URLField()
    def __str__(self):
        return self.producto
class Correo(models.Model):
    email = models.EmailField()
class Existencias(models.Model):
    pass