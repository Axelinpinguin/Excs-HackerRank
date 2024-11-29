escribir=input('Oración que desees escribir: ')
palabra=int(input('Ingrese el numero de veces a repetir: '))

for i in range(1,palabra+1):
    print(f'{i}.- {escribir}')
