from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel):
    username: str
    nombre: str
    apellido: str
    email: str
    password: str


database_users = {
    "camilo24": UserInDB(**{"username": "camilo24",
                            "nombre": "Camilo",
                            "apellido": "lopez",
                            "email": "camilo@gmail.com",
                            "password": "1234"

                            }),
    "andres18": UserInDB(**{"username": "andres18",
                            "nombre": "andres",
                            "apellido": "lopez",
                            "email": "andres@gmail.com",
                            "password": "1234"
                            }),
}


def get_users():
    return database_users


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    return None
