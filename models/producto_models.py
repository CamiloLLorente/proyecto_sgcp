from pydantic import BaseModel


class ProductoIn(BaseModel):
    codigo: str
    nombre: str


class ProductoOut(BaseModel):
    nombre: str
    precio: float
    cantidad: int
