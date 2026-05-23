from fastapi import FastAPI

mi_app= FastAPI () 

@mi_app.get ("/proyecto")

def mensaje ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar"}


lista= ["Yoberson","William","Suns","daniela","kamila","Quiroga"]
@mi_app.get ("/clientes")
def Personas ():
    return {"clientes": lista}