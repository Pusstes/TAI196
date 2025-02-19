from fastapi  import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='Api de tareas',
    description='Pracrica 4 de TAI 196',
    version='1.0.1'
)

tareas = [
    {'id': 1, 'nombre': 'Estudiar', 'descripcion': 'Estudiar para el examen', 'vencimiento': '2025-03-10', 'estado': 'Completada'},
    {'id': 2, 'nombre': 'Comer', 'descripcion': 'Comer una pizza de  la tombola', 'vencimiento': '2025-02-22', 'estado': 'pendiente'},
    {'id': 3, 'nombre': 'Dormir', 'descripcion': 'Dormir 8 horas', 'vencimiento': '2025-02-20', 'estado': 'pendiente'},
    {'id': 4, 'nombre': 'Correr', 'descripcion': 'Correr 5 km', 'vencimiento': '2025-02-20', 'estado': 'pendiente'},
    {'id': 5, 'nombre': 'Acabar lo de Isay', 'descripcion': 'Terminar la  practica 4', 'vencimiento': '2025-02-19', 'estado': 'Completada'},
    {'id': 6, 'nombre': 'Leer berserk', 'descripcion': 'Leer el capitulo   140', 'vencimiento': '2025-02-20', 'estado': 'Completada'}
]

# endPoint para mostrar la lista de tareas
@app.get('/tareas/', tags=['Operaciones de las Tareas'])
def consultar_tareas():
    return {'Tareas Registradas': tareas}