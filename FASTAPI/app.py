from fastapi import FastAPI, HTTPException,Depends
from fastapi.responses import JSONResponse
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middleweres import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Gerardo Alberto ramirez',
    version='1.0.1'
)

#creamos la base de datos
Base.metadata.create_all(bind=engine)


usuarios= [
    {'id':1, 'nombre':'Gerardo', 'edad': 20, 'correo':'gerardo@gmail.com'},
    {'id':2, 'nombre':'Alberto', 'edad': 20, 'correo':'gerardo@gmail.com'},
    {'id':3, 'nombre':'Ramirez', 'edad': 20, 'correo':'gerardo@gmail.com'},
    {'id':4, 'nombre':'Gerardo Alberto', 'edad': 23, 'correo':'gerardo@gmail.com'},
    {'id':5, 'nombre':'America', 'edad': 24, 'correo':'gerardo@gmail.com'},
    {'id':6, 'nombre':'Chivas', 'edad': 25, 'correo':'gerardo@gmail.com'},
]

@app.post('/auth/', tags=['Autenticacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'gerardo@example.com' and autorizado.password == '123456789':
        token = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {'Aviso':'Usuario no autorizado'}
    

    
    
  
        
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
@app.get('/usuarios/', dependencies= [Depends(BearerJWT())], response_model= List[modelUsuario] ,tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

# end point para guardar un usuario tipo post
@app.post('/usuario/',response_model= modelUsuario ,tags=['Operaciones CRUD']) #se agrega el modelo de respuesta
def guardarUsuario(usuarionuevo: modelUsuario): #se agrega el modelo de entrada
    db = Session() #se crea la sesion
    try: #se intenta guardar el usuario
        db.add(User(**usuarionuevo.model_dump())) #se agrega el usuario a la base de datos
        db.commit() #se guarda el usuario
        return JSONResponse(status_code=201, content={'mensaje':'Usuario guardado', 'usuario':usuarionuevo.model_dump()}) #se retorna el usuario guardado
    except Exception as e: #en caso de error se retorna un mensaje de error
        db.rollback() #se deshace la transaccion
        return JSONResponse(status_code=500, content={'mensaje':'Error al guardar el usuario', 'error':str(e)})
    finally:
        db.close()

# end point para actualizar un usuario tipo put
# se recibe un parametro de tipo modelUsuario
# se valida si el usuario existe en la base de datos
# se recorre la lista de usuarios y se actualiza el usuario
# se retorna el usuario actualizado
""" @app.put('/usuario/{id}',response_model=modelUsuario ,tags=['Operaciones CRUD'])
def actualizarUsuario(id: int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr['id'] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail='Usuario no encontrado')


@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def borrarUsuario(id: int):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return {'mensaje':'Usuario eliminado'}
    raise HTTPException(status_code=400, detail='Usuario no encontrado') """

@app.get('/TAI196/FASTAPI/DB/usuarios.sqlite', tags=['OPERACIONES CRUD'])
def ConsultarTodos():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500, content={'mensaje':'No fue posible hacer la consulta', 'error':str(x)})
    
    finally:
        db.close()
        
@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consultaUsuario(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={'mensaje':'Usuario no encontrado'})
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500, content={'mensaje':'No fue posible hacer la consulta', 'error':str(x)})
    
    finally:
        db.close()
