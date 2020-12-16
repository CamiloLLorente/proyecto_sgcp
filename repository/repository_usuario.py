from models import user_models
from db import user_db


def get_usuario_out():
    lista_usuario_out = []
    usuarios = user_db.get_users()
    for usuario_key, usuario_value in usuarios.items():
        usuario_out = user_models.UserOut(
            username=usuario_value.username, email=usuario_value.email)
        lista_usuario_out.append(usuario_out)
    print(lista_usuario_out)
    return lista_usuario_out


def get_usuario_login(username: str):
    usuario_value = user_db.get_user(username)
    if usuario_value is None:
        return None
    usuario_out = user_models.UserOut(
        username=usuario_value.username, email=usuario_value.email)
    return usuario_out
