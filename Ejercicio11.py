#Bi
def validacion_contraseña ():
    
    contraseña_sistema  = "admin123"

    Contraseña_usuario = input ("ingrese contraseña")

    if Contraseña_usuario == contraseña_sistema:
        print("Contraseña correcta")
    else:
        print("contraseña incorrecta")        

validacion_contraseña()
    