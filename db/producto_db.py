from typing import Dict
from pydantic import BaseModel


class ProductoInDB(BaseModel):
    codigo: str
    nombre: str
    precio: float
    cantidad: int
    seccion:str
 


database_producto = {
    "1001": ProductoInDB(**{"codigo": "1001",
                            "nombre": "Mause",
                            "precio": 12000,
                            "cantidad": 5,
                            "seccion": "Tecnologia"
                            }),
    "1002": ProductoInDB(**{"codigo": "1002",
                            "nombre": "Monitor",
                            "precio": 14000,
                            "cantidad": 9,
                            "seccion": "Tecnologia"
                            }),

}


def get_productos():
    return database_producto


def get_producto(codigo: str):
    if codigo in database_producto.keys():
        return database_producto[codigo]
    return None
