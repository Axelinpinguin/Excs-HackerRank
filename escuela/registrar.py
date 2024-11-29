print()
lista_registro=[]
login=True
while login:
    decision=input('''Bienenido al cielo
1) Registrar\n2) Modificar\n3) Salir\nSelecciona la opción a realizar: ''')
    print()
    if decision=='1':
        nombre=input('Registra tu\nNombre: ')
        lista_registro.append(nombre)
        a_paterno=input('Apellido paterno: ')
        lista_registro.append(a_paterno)
        a_materno=input('Apellido materno: ')
        lista_registro.append(a_materno)
        login_genero=True
        while login_genero:
            genero=input('Genero (F/M/O): ')
            if genero=='F':
                lista_registro.append(genero)
                login_genero=False
            elif genero=='M':
                lista_registro.append(genero)
                login_genero=False
            elif genero=='O':
                lista_registro.append(genero)
                login_genero=False
            else:
                print('Solo letras mayusculas')
        email=input('Email: ')
        lista_registro.append(email)
        print(lista_registro)
    elif decision=='2':
        if len(lista_registro)==0:
            print('Tienes que tener al menos un registro para poder modificar.')
            print()
        else:
            verificar_nombre=input('Ingresa el correo de la persona que desees modificar: ')
        if lista_registro.count(verificar_nombre):
            login_modificar=True
            while login_modificar:
                selec_modificar=input('''1)Nombre\n2)Apellido paterno\n3)Apellido materno\n4)Género (F/M/O)\n5)Email\n6)Cancelar\nSeleccione la opción que desee modificar: ''')
                if selec_modificar=='1':
                    nuevo_nombre=input('Profaa creo que si llega al 50%, no? ')
                elif selec_modificar=='2':
                    print('hola2')
                elif selec_modificar=='3':
                    print('hola3')
                elif selec_modificar=='4':
                    print('hola4')
                elif selec_modificar=='5':
                    print()
                elif selec_modificar=='6':
                    print('Haz cancelado')
                    print()
                    login_modificar=False
                else:
                    print('Elija sólo números respectivos')
        else:
            print('No se ha encontrado el correo de la persona que desea modificar.')
            print()
    elif decision=='3':
        print('Profaa creo que si llega al 50%, no? ')
        login=False
    else:
        print('Ingresa sólo numeros del 1 al 3')
        print()