i = 0
while i < 10:
    print(i)

    i += 1
ingresar = True
while ingresar:
    valor = int(input('Ingresa un numero mayor a 50: '))
    if valor > 50:
        ingresar = False
        print('has cumplido el requisito')

    