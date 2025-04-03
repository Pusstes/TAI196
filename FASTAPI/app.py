from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth
from fastapi.middleware.cors import CORSMiddleware

#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Gerardo Alberto ramirez',
    version='1.0.1'
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#creamos la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)


@app.get("/",  tags=["Inicio"]) 
def main(): #
    return {"Hello FastAPI": "Gerardo Alberto Ramirez"}

    
  
        

