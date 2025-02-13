from fastapi import FastAPI, HTTPException

from typing import Optional

#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Gerardo Alberto ramirez',
    version='1.0.1'
)

usuarios= [
    {'id':1, 'nombre':'Gerardo', 'edad': 20},
    {'id':2, 'nombre':'Alberto', 'edad': 20},
    {'id':3, 'nombre':'Ramirez', 'edad': 20},
    {'id':4, 'nombre':'Gerardo Alberto', 'edad': 23},
    {'id':5, 'nombre':'America', 'edad': 24},
    {'id':6, 'nombre':'Chivas', 'edad': 25}
]
        
# #generamos nuestro primer endpoint 
# # endpoint tipo get 
# @app.get('/', tags=['Inicio'])
# def main():
#     return {'hello FastAPI':'Gerardo Alberto'}

# @app.get('/promedio', tags=['Mi Calificacion TAI'])
# def promedio():
#     return 5*2

# # end point parametro obligatorio
# @app.get('/usuario/{id}', tags=['Parametro obligatorio'])
# def consultaUsuario(id: int):
#     return {'se encontro el usuario': id}

# # endPoint parametro opcional
# @app.get('/usuario2/', tags=['Parametro Opcional'])
# def consultarUsuarioOpcional(id: Optional[int] = None):
#     if id is not None:
#         for usuario in usuarios:
#             if usuario['id'] == id: 
#                 return {'Usuario encontrado': usuario}
#         return {'Mensaje':f'No se encontrado el id: {id}'}
#     else:
#         return{'mensaje': 'No hay usuarios registrados'}
    
#     #endpoint con varios parametro opcionales
# @app.get("/usuarios/", tags=["3 parámetros opcionales"])
# async def consulta_usuarios(
#     usuario_id: Optional[int] = None,
#     nombre: Optional[str] = None,
#     edad: Optional[int] = None
# ):
#     resultados = []

#     for usuario in usuarios:
#         if (
#             (usuario is None or usuario["id"] == usuario_id) and
#             (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
#             (edad is None or usuario["edad"] == edad)
#         ):
#             resultados.append(usuario)

#     if resultados:
#         return {"usuarios_encontrados": resultados}
#     else:
#         return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."+str(usuario_id)+str(nombre)+str(edad)}

# end poin consultar todos los usuarios
@app.get('/usuarios/', tags=['Operaciones CRUD'])
def ConsultarTodos():
    return {'Usuarios Registrados':usuarios}

# end point para guardar un usuario tipo post
@app.post('/usuario/', tags=['Operaciones CRUD'])
def guardarUsuario(usuarionuevo: dict):
    for usr in usuarios:
        if usr['id'] == usuarionuevo.get('id'):
            raise HTTPException(status_code=400, detail='El usuario ya esta registrado')
    usuarios.append(usuarionuevo)
    return {'mensaje':'Usuario registrado'}