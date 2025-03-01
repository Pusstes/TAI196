import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

# Función que genera un token a partir de un diccionario de datos
# Parámetros:
def createToken(datos: dict):
    token: str = jwt.encode(payload=datos, key='secretkey', algorithm='HS256')
    return token

def validateToken(token: str):
    try:
        data: dict = jwt.decode(jwt=token, key='secretkey', algorithms=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail='El Token expiro')
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail='Token NO Autorizado')