tamano=int(input(''))
if 0<tamano<=100:
    conjunto = list(map(int, input().split())) #aplica una funcion a un valor deseado 
    if len(conjunto) > tamano:
        print("Ingresa los mismos numeros al tamano deseado")
    else:
        positives=negatives=zero=0
        for i in conjunto:
            if i>0:
                positives+=1
            elif i<0:
                negatives+=1
            else:
                zero += 1
        fra_negative = negatives/tamano
        fra_positive = positives/tamano
        fra_zero = zero/tamano
        print(f'{fra_positive:.6f}')
        print(f'{fra_negative:.6f}')
        print(f'{fra_zero:.6f}')
else:
    print('El tamano solo debe ser entre 1 y 99')