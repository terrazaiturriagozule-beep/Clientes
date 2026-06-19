from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

mi_app= FastAPI () 

@mi_app.get ("/proyecto")

def mensaje ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar.."}


lista= ["Yoberson","William","Suns","daniela","kamila","Quiroga"]
@mi_app.get ("/clientes")
def Personas ():
    return {"clientes": lista}

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str