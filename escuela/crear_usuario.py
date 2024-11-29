print()

usuarios=[]
contraseñas=[]
letras_min=0
numeros=0
letras_mayus=0
caracteres=0
entrar=True
while entrar:
    decision=input('c=Crear usuario\ni=Iniciar sesión\ns=Salir\nSeleccione la opcion que desee realizar: ')
    if decision=='c':
        print('Crear usuario')
        usuario=input('Ingresa un nombre de usuario válido: ')
        if len(usuario) >=6 and len(usuario)<=10:
            for caracteres_usuario in usuario:
                if caracteres_usuario.islower():
                    letras_min+=1
                if caracteres_usuario.isdigit():
                    numeros+=1
                if caracteres_usuario.isalnum()==False:
                    caracteres+=1
            if letras_min>0 and numeros>0 and caracteres==False:
                entrar=False
    elif decision=='i':
        print('Iniciar sesion')
    elif decision=='s':
        print('salir')
        entrar=False          
    else:
        print()
        print('Sólo "c", "i" y "s" minuscula')
        print()