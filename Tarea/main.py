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
    {'id': 6, 'nombre': 'Leer berserk', 'descripcion': 'Leer el capitulo   140', 'vencimiento': '2025-02-20', 'estado': 'Completada'},
    {'id': 7, 'nombre': 'Tarea  de prueba  a borrar', 'descripcion': 'se borrara', 'vencimiento': '2025-02-20', 'estado': 'pendiente'},
]

# endPoint para mostrar la lista de tareas
@app.get('/tareas/', tags=['Operaciones de las Tareas'])
def consultar_tareas():
    return {'Tareas Registradas': tareas}

# endPoint para borrar una tarea por id
@app.delete('/tareas/{id}', tags=['Operaciones de las Tareas'])
def borrar_tarea(id: int):
    for tarea in tareas:
        if tarea['id'] == id:
            tareas.remove(tarea)
            return {'Tarea Eliminada': tarea}
    raise HTTPException(status_code=400, detail=f'No se encontro la tarea con el id: {id}')

# end point  para guardar una tarea nueva
@app.post('/tareas/', tags=['Operaciones de las Tareas'])
def guardar_tarea(tarea: dict):
    for t in tareas:
        if t['id'] == tarea['id']:
            raise HTTPException(status_code=400, detail=f'Ya existe una tarea con el id: {tarea["id"]}')

    tareas.append(tarea)
    return {'Tarea Guardada': tarea}

# endPoint para obtener una tarea por id
@app.get('/tareas/{id}', tags=['Operaciones de las Tareas'])
def consultar_tarea(id: int):
    for tarea in tareas:
        if tarea['id'] == id:
            return {'Tarea Encontrada': tarea}
    raise HTTPException(status_code=400, detail=f'No se encontro la tarea con el id: {id}')

# end point para actualizar una tarea
@app.put('/tareas/{id}', tags=['Operaciones de las Tareas'])
def actualizar_tarea(id: int, tarea: dict):
    for t in tareas:
        if t['id'] == id:
            tareas.remove(t)
            tareas.append(tarea)
            return {'Tarea Actualizada': tarea}
    raise HTTPException(status_code=400, detail=f'No se encontro la tarea con el id: {id}')