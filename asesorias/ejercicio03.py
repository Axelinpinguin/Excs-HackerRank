login=True
while login:
    numero_tabla=(input('\nIngresa el numero de la tabla que desees multiplicar: '))
    if numero_tabla.isdigit():
        print()
        for i in range(1,11):
            numero=int(numero_tabla)
            mult=i*numero
            print(f'Resultado {i}x{numero_tabla}: {mult}')
            login=False
    else:
        print('\nSolo acepta numeros')