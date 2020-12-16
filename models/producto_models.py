from pydantic import BaseModel


class ProductoIn(BaseModel):
    codigo: str
    nombre: str


class ProductoOut(BaseModel):
    codigo:str
    nombre: str
    precio: float
    cantidad: int
    seccion:str
