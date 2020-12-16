from db import producto_db, user_db
from models import producto_models, user_models
from repository import repository_producto, repository_usuario
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://proyecto-sgcp.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# productos

# obtener todos los producos


@api.get("/productos")
async def get_productos():
    return repository_producto.get_productos_out()


# obtener un producto por medio del codigo
@api.get("/producto/{cod_producto}")
async def get_producto_by_cod(cod_producto: str):
    if producto_db.get_producto(cod_producto) is None:
        raise HTTPException(
            status_code=400, detail="error, no existe este producto")
    return producto_db.get_producto(cod_producto)

# crear un nuevo producto


@api.post("/producto/nuevo")
async def new_producto(producto: producto_db.ProductoInDB):
    producto_db.database_producto[producto.codigo] = producto
    return producto_db.get_productos()

# eliminar un producto


@api.delete("/producto/{cod_producto}")
async def delete_producto(cod_producto: str):
    if producto_db.get_producto(cod_producto) is None:
        raise HTTPException(
            status_code=400, detail="error, no existe este producto")
    del producto_db.database_producto[cod_producto]
    return producto_db.get_productos()

# actualizar un producto


@api.put("/producto/{producto_id}")
async def update_producto(producto_id: str, producto: producto_db.ProductoInDB):
    producto_db.database_producto[producto_id] = producto
    return producto_db.get_productos()

# usuarios

# obtener todos los usuarios


@api.get("/usarios")
async def get_usuarios():
    return user_db.get_users()

# obtener un usuario mediante el username


@api.get("/usario/{username}")
async def get_usuarios(username: str):
    if user_db.get_user(username) is None:
        raise HTTPException(
            status_code=400, detail="error, no existe el usuario")
    return user_db.get_user(username)

# ver si un usuario esta logueado


@api.post("/usuario/login")
async def usuario_login(usuario: user_models.UserIn):
    if user_db.get_user(usuario.username) is None:
        raise HTTPException(
            status_code=400, detail="error, no existe el usuario")
    usuario_db = user_db.get_user(usuario.username)
    if (usuario.username != usuario_db.username) or (usuario.password != usuario_db.password):
        raise HTTPException(
            status_code=400, detail="error, El usuario o la contraseña no coincide")
    return repository_usuario.get_usuario_login(usuario.username)

# crear un nuevo usuario


@api.post("/usuario/nuevo")
async def nuevo_usuario(usuario: user_db.UserInDB):
    if user_db.get_user(usuario.username) is None:
        user_db.database_users[usuario.username] = usuario
        return user_db.get_users()
    raise HTTPException(
        status_code=400, detail="El username ya existe")

# actualizar usuario


@api.put("/usuario/{username}")
async def update_usuario(username: str, usuario: user_db.UserInDB):
    user_db.database_users[username] = usuario
    return user_db.get_users()


@api.delete("/usuario/{username}")
async def delete_usuario(username: str):
    if user_db.get_user(username) is None:
        raise HTTPException(
            status_code=400, detail="error, El usuario no existe")
    del user_db.database_users[username]
    return user_db.get_users()
