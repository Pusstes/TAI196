from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from tokenGen import createToken
from fastapi import APIRouter

routerAuth = APIRouter()


@routerAuth.post('/auth/', tags=['Autenticacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'gerardo@example.com' and autorizado.password == '123456789':
        token = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {'Aviso':'Usuario no autorizado'}
    

    