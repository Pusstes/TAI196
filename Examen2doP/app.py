from fastapi import FastAPI, HTTPException,Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List

envios = [
    {"CodigoPostal": "76000", "Destino": "Queretaro", "Peso": 2},
    {"CodigoPostal":"2600", "Destino": "Aguascalientes", "Peso": 10},
    {"CodigoPostal:": "36000", "Destino": "Guanajuato", "Peso": 5},
    {"CodigoPostal": "50000", "Destino": "Toluca", "Peso": 1},
    {"CodigoPostal": "2000", "Destino": "CDMX", "Peso": 3},
    {"CodigoPostal": "24000", "Destino": "Leon", "Peso": 6},
    {"CodigoPostal": "23000", "Destino": "Zacatecas", "Peso": 8},
    {"CodigoPostal": "25000", "Destino": "San Luis Potosi", "Peso": 9},
    {"CodigoPostal": "28000", "Destino": "Colima", "Peso": 7},
    {"CodigoPostal": "29000", "Destino": "Tepic", "Peso": 4},     
]

app = FastAPI(
    title='Envios', 
    description='Gerardo Alberto ramirez',
    version='1.0.1'
)

class modelEnvio(BaseModel):
    CodigoPostal: str = Field(...,min_length=5, max_length=55, description='Codigo Postal')
    Destino: str = Field(...,min_length=6, max_length=55, description='Destino')
    Peso: int = Field(...,gt=0, lt=500, description='Peso')
    
#end point para ver todos los envios
@app.get('/envios/',tags=['Operaciones CRUD de Envios'])
def ConsultarTodos():
    return envios

#end point para borrar un envio por codigo postal
@app.delete('/envio/{CodigoPostal}', tags=['Operaciones CRUD de Envios'])
def ConsultarEnvio(CodigoPostal: str):
    for envio in envios:
        if envio.get("CodigoPostal") == CodigoPostal:
            envios.remove(envio)
            return {'mensaje': 'Envio eliminado'}
    raise HTTPException(status_code=400, detail='Envio no encontrado')



#end point para guardar un envio tipo post
@app.post('/envio/', tags=['Operaciones CRUD de Envios'])
def guardarEnvio(envionuevo: modelEnvio):
    for envio in envios:
        if envio.get("CodigoPostal") == envionuevo.CodigoPostal:
            raise HTTPException(status_code=400, detail='El envio ya esta en camino')

    envios.append(envionuevo)  # Convierte Pydantic model a diccionario
    return {'mensaje': 'Envio guardado'}

        
  
