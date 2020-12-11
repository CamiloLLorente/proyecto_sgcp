from models import producto_models
from db import producto_db


def get_productos_out():
    lista_productos_out = []
    productos = producto_db.get_productos()
    for producto_key, productos_value in productos.items():
        producto_out = producto_models.ProductoOut(
            nombre=productos_value.nombre, precio=productos_value.precio, cantidad=productos_value.cantidad)
        lista_productos_out.append(producto_out)
    print(lista_productos_out)
    return lista_productos_out
