from pydantic import BaseModel, Field, EmailStr

#creamos una clase para el modelo de usuario
class modelUsuario(BaseModel):
    name: str = Field(...,min_length=3, max_length=55, description='Nombre debe contener solo letras  y letras')
    age: int = Field(...,gt=0, lt=100, description='Edad debe ser un numero positivo')
    email:str = Field(..., min_length=3, max_length=55, description='Correo electronico', pattern="^[\w\.-]+@[\w\.-]+\.\w+$", example="example@gmail.com")
    
    #creamos una clase para el modelo de autenticacion que servira para el login
class modelAuth(BaseModel):
    correo:EmailStr
    password:str = Field(...,min_length=8, strip_withespace=True, description='Contraseña debe contener al menos 8 caracteres')
    