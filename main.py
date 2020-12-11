from db import producto_db
from models import producto_models
from repository import repository_producto


from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/productos")
async def get_productos():
    return producto_db.get_productos()


@app.get("/productos/out")
async def get_productos():
    return repository_producto.get_productos_out()


@app.get("/producto/{cod_producto}")
async def get_producto_by_cod(cod_producto: str):
    if producto_db.get_producto(cod_producto) is None:
        raise HTTPException(
            status_code=400, detail="error, no existe este producto")
    return producto_db.get_producto(cod_producto)


@app.post("/producto/nuevo")
async def new_producto(producto: producto_db.ProductoInDB):
    producto_db.database_producto[producto.codigo] = producto
    return producto_db.get_productos()


@app.delete("/producto/{cod_producto}")
async def delete_producto(cod_producto: str):
    del producto_db.database_producto[cod_producto]
    return producto_db.get_productos()


@app.put("/producto/{producto_id}")
async def update_producto(producto_id: str, producto: producto_db.ProductoInDB):
    producto_db.database_producto[producto_id] = producto
    return producto_db.get_productos()
