from django.shortcuts import render
from scrapp import models
from bs4 import BeautifulSoup
from django.core.mail import EmailMessage
import urllib.request
from django.contrib import messages

# Create your views here.
def buscarTexto(texto, elemento):
    busqueda = texto.find(elemento)
    if busqueda != -1:
        return True
    else:
        return False
def Inicio(request):
    producto = models.Producto.objects.all()
    contexto = {
        'productos':producto
    }
    return render(request, 'index.html', contexto)


def buscarProducto(request):
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
                    messages.success(request, descripcion)
                    lista_productos.append(producto.producto)
                    lista_url.append(producto.url_de_busqueda)
                    messages.success(request, descripcion)

                else:
                    descripcion1 = "No %s  encontrado, o no existe conexion a internet" % producto.producto
                    messages.error(request, descripcion1)

        except:
            descripcion1 = "No productos encontrados, o no existe conexion a internet"
            messages.error(request, descripcion1)
            return render(request, 'index.html', contexto)

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

    return render(request, 'index.html')



