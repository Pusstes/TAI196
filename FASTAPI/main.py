from fastapi import FastAPI 
# importamos la libreria para permitir datos opcionales
from typing import Optional

# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI(
    title='Mi primer API 196',
    description='Estrella Cuellar',
    version='1.0.1'
)

#Creamos una lista para la base de datos 
usuarios=[
    {'id':1, 'nombre':'Estrella', 'edad':20},
    {'id':2, 'nombre':'Lu', 'edad':20},
    {'id':3, 'nombre':'Lalo', 'edad':21},
    {'id':4, 'nombre':'Domi', 'edad':20},
]


# endpoint de arranque 
@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola FASTAPI':'EstrellaCuellar'}

@app.get('/promedio', tags=['Mi claificaión'])
def promedio():
    return {'Promedio': 9.9}

#endpoint obligatorio
@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consultarusuario(id:int):
    #conectamosBD
    #hacemos consulta retornamos resultset 
    return{'Se encontro el usuario': id}

#endpoint opcional
