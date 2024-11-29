def fibonacci(n):
    lista=[]
    num1=0
    num2=1
    for i in range (0,n):
        num1=num1+num2
        num2=num1-num2
        lista.append(num2)
    return lista

numero=int(input('numero:'))
lista_fibonacci=(fibonacci(numero))
print(lista_fibonacci)

def mostrar_ultimo_digito(p):
    ultimo=fibonacci(p)
    print(ultimo[p-1])
mostrar_ultimo_digito(numero)