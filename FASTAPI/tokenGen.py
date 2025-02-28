import jwt

# Función que genera un token a partir de un diccionario de datos
# Parámetros:
def createToken(datos: dict):
    token: str = jwt.encode(payload=datos, key='secret', algorithm='HS256')
    return token