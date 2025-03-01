from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from tokenGen import validateToken


class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):       #call es un metodo que se ejecuta cuando se llama a la clase
        auth= await super().__call__(request)      #auth es un diccionario que contiene el token que se obtiene del request
        data =  validateToken(auth.credentials) #data es un diccionario que contiene los datos del token
        
        if not isinstance(data, dict):     #si data no es un diccionario
            raise HTTPException(status_code=403, detail='Formato de token no valido')
        
        if data.get('correo')!= 'gerardo@example.com': #si el correo no es igual a rl correo estatico
            raise HTTPException(status_code=403, detail='Credenciales NO Validadas')