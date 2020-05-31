from django.core.management.base import BaseCommand
from django.shortcuts import render
from scrapp import models
from bs4 import BeautifulSoup
from django.core.mail import EmailMessage
import urllib.request
from django.contrib import messages
def buscarTexto(texto, elemento):
    busqueda = texto.find(elemento)
    if busqueda != -1:
        return True
    else:
        return False
class Command(BaseCommand):
    help = 'Busca productos en las tienda de envio.cu'

    def handle(self, *args, **options):

        productos = models.Producto.objects.all()
        contexto = {
            'productos': productos
        }
        lista_productos = []
        lista_url = []

        for producto in productos:
            url = producto.url_de_busqueda
            try:
                datos = urllib.request.urlopen(url).read().decode()
                soup = BeautifulSoup(datos, 'lxml')
                titulos = soup.find_all("div", class_='thumbTitle')

                for titulo in titulos:
                    if buscarTexto(titulo.text, producto.producto):
                        descripcion = "Producto %s encontrado. Espere un email" % producto.producto

                        lista_productos.append(producto.producto)
                        lista_url.append(producto.url_de_busqueda)


                    else:
                        descripcion1 = "No %s  encontrado, o no existe conexion a internet" % producto.producto


            except:
                descripcion1 = "No productos encontrados, o no existe conexion a internet"


                #     Enviar correo
        if lista_productos.__len__() > 0:

            email = EmailMessage(
                "Urgente encontre productos en las tiendas",
                "De Aplicacion de busqueda de productos\n\nEscribio: Encontre estos productos\n\n"
                "%s " % lista_productos + "en estas url: %s" % lista_url,
                "no-contestar@inbox.mailtrap.io",
                ['adrianglez2203@gmail.com', 'adisgs9128gmail.com'],
                reply_to=['adriangle2203@gmail.com']
            )
            email.send()
            print(lista_productos)
        else:
            pass




