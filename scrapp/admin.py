from django.contrib import admin
from scrapp.models import Correo, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['producto','url_de_busqueda']

admin.site.register(Correo)
admin.site.register(Producto,ProductoAdmin)