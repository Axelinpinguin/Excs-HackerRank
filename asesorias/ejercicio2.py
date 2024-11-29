import os
contador=1
contadornuevo=3
ingrese_usuario=input('Ingresa tu usuario: ')
crea_contraseña=input('Contraseña: ')
login=True
while login:
    ingresa_contraseña=input('Ingresa contraseña: ')
    if ingresa_contraseña==crea_contraseña:
        os.system('cls')
        print('Contraseña correcta, bienvenido')
        login=False
    else:
        if contador<3:
            contadornuevo-=1
            os.system('cls')
            print(f'Error, intenta de nuevo te quedan {contadornuevo} intentos')
        else:
            os.system('cls')
            print('Has sobrepasado el límite')
            login=False
    contador+=1