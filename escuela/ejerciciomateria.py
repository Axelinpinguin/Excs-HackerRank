listamateria=[]
calificacion=[]
agregar = True
while(agregar):
    nuevamateria = input('Escribe otra materia : ')
    calificacion = float(input('Escribe tu calificacion: '))
    listamateria.append(nuevamateria)
    print(listamateria)
    print(calificacion)
    opc = input('¿Quieres seguir agregando materia? s/n:  ')
    if opc.upper()== 'N':
        agregar = False
for nombre in listamateria:
    print('--------------------------------------------')
    print(nombre,'tu calificacion es: ', calificacion)
    if calificacion >= 9:
        print('felicidades te vas a harvard')
    elif calificacion <= 9 :
        print('te quedas en la facultad')
