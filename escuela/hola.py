resultado=0
cont=0
num1=int(input('Cuantos números deseas sumar: '))
while cont <num1:
    num2=float(input('Igrese el numero a sumar: '))
    resultado+=num2
    cont+=1
print(f'La suma es: {resultado}')
    