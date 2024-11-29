listaapellidoP = ['a','b','c']
listanombre = []
listaapellidoM =[]
genero =[]
gmail = []
listacompleta = []
listacompleta= listanombre + listaapellidoP + listaapellidoM + genero + gmail
login = True
while login:
    print()
    print("Bienvenido al registro en que lo podemos atender")
    print('''
    1) registrar
    2) Modificar
    3) Salir
        ''')
    opcion = int(input("Selecciona una opción: "))  
    if opcion ==1 :
        nombre=(input('¿cual es su nombre ? : '))
        listanombre.append(nombre)
        ApellidoP=(input('¿cual es su Apellido parterno ? : '))
        listaapellidoP.append(ApellidoP)
        ApellidoM=(input('¿cual es su Apellido Materno ? : '))
        listaapellidoM.append(ApellidoM)
        gen = (input('¿cual es su genero (F/M/O)? : '))
        genero.append(gen)
        gmai= (input('¿cual es su correo electronico? :'))
        gmail.append(gmai)
        datos=(f'tus datos se guardaron correctamente {(listacompleta)} ')
      
    elif opcion == 2 :
         confirmar= len(gmail)
         if confirmar==0: 
              print('Debes de ingresar primeros los datos antes de modificar : ')
         else:
              login = True
              while login:
                   correo = (input(f'¿cual es tu correo? :'))
                   if gmail.count(correo):
                    menus=True
                    while menus:
                         print("dijame que desea modificar")
                         print('''
                         1) Nombre
                         2) Apellido Paterno
                         3) apellido MAterno
                         4) genero
                         5)gmail
                         6)cancelar
                         ''')
                         opcion = int(input("Selecciona una opción del 1 al 6 : "))
                         if opcion ==1:
                              nombre=(input('¿cual es su nombre ? : '))
                              listanombre.append(nombre)
                              print(listanombre)
                         elif opcion == 2 :
                              ApellidoP=(input('¿cual es su Apellido parterno ? : '))
                              listaapellidoP.append(ApellidoP)
                         elif opcion ==3 :
                              ApellidoM=(input('¿cual es su Apellido Materno ? : '))
                              listaapellidoM.append(ApellidoM)
                         elif opcion == 4 :
                             gen = (input('¿cual es su genero (F/M/O)? : '))
                             genero.append(gen)
                         elif opcion == 5:
                              gmai= (input('¿cual es su correo electronico? :'))
                              gmail.append(gmai)
                         elif opcion == 6 :
                              print('has cancelado las modificacion : ')
                              menus = False
                         else:
                             print('seleccione una opcion')
                             
    elif opcion == 3 :
          print('vuelva pronto... :)')
         
          login = False
    else:
        print('por favor selecciona una opcion...')

