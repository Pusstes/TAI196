from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth


#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Gerardo Alberto ramirez',
    version='1.0.1'
)

#creamos la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)


@app.get("/",  tags=["Inicio"]) 
def main(): #
    return {"Hello FastAPI": "Gerardo Alberto Ramirez"}

    
  
        

