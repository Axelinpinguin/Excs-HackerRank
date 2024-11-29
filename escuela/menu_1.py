#Felipe Garcia Duran / julio cesar de la cruz molina


lista_usuarios=[]
lista_contraseñas=[]
minusculas_usuario=0
mayusculas_usuario=0
numeros_usuario=0
simbolos_usuario=0
letras_usuario=0
espacio=0
intentos=0
entrar=True
while entrar:
    print('bienvenido al portal wikiwoon :).... ')
    print('''Menu de opciones: 
c) crear usuario
i) iniciar sesion 
s) salir''')
    print()
    print('ingrese la letra del inciso....')
    opc=input('selecciona una opcion a realizar: ')
    opc=opc.lower()
    if opc=='c':
        usuario=input('ingrese un usuario valido: ')
        if len(usuario)>=6 and len(usuario)<=10:
            for caracteres in usuario:
                if caracteres.isalpha():
                    letras_usuario +=1
                if caracteres.islower():
                    minusculas_usuario += 1
                if caracteres.isupper():
                    mayusculas_usuario +=1
                if caracteres.isdigit():
                    numeros_usuario += 1
                if caracteres.isalnum==False:
                    simbolos_usuario += 1
        if letras_usuario>0 and minusculas_usuario>0 and numeros_usuario>0 and simbolos_usuario==0 and mayusculas_usuario==0 and usuario[0].islower()==True and usuario[-1].isdigit()==True:
            print('usuario válido..')
            flag=True
            while flag: 
                vecesQueAparece=lista_usuarios.count(usuario)
                if vecesQueAparece==0:
                    print(f'veces que aparece el usuario:', vecesQueAparece)
                    lista_usuarios.append(usuario)
                    contraseña=input('Ingresa una contraseña: ')
                    if len(contraseña)<8:
                        print('contraseña muy corta..no es segura')
                    elif len(contraseña)>=8:
                        for caracteres in contraseña:
                            if caracteres.count(' ')>0:
                                espacio += 1
                    ingresardenuevo=True
                    while ingresardenuevo==True:
                        contraseña=input('ingresa una contraseña valida: ')
                        if contraseña[0].isupper()==True and contraseña[-1].isalnum()==False and espacio==0 :
                            lista_contraseñas.append(contraseña)
                            print('usuario registrado exitosamente...')
                            ingresardenuevo=False
                            flag=False
                else: 
                    print('El usuario ya existe, registra uno nuevo: ')
                    flag=False
        else:
            print('usuario invalido... selecciona denuevo la opcion a realizar..')
    elif opc =='i':
        vecesQueAparece= len(lista_usuarios)
        if vecesQueAparece==0: 
            print('Debes crear una cuenta para poder iniciar sesión: ')
        else:
            validos=True
            while validos:
                pedir_usuario=input('introdusca un usuario: ')
                pedir_contraseña=input('introdusca la contraseña: ')
                intentos+= 1
                if lista_usuarios.count(pedir_usuario) and lista_contraseñas.count(pedir_contraseña):
                    index_usuario=lista_usuarios.index(pedir_usuario)
                    index_contra= lista_contraseñas.index(pedir_contraseña)
                    print(index_usuario)
                    if  index_usuario==index_contra:
                        print(f'..BIENVENIDO... ;) ', pedir_usuario)
                        validos=False
                        entrar=False
                else:
                    print()
                    print('las credenciales no coinciden =)--')
                    if intentos == 1:
                         print('intenta de nuevo tienes 3 oportunidades: ')
                    elif intentos==2:
                        print('intenta de nuevo tienes 2 intentos: ')
                    elif intentos==3:
                        print('solo te queda un intento no te equivoques: ')
                    elif intentos>=4:
                        print('te invito a crear una nueva cuenta')
                        validos=False
    elif opc =='s':
        print('vuelva pronto... :)')
        entrar=False
    else:
        print('por favor selecciona una opcion...')