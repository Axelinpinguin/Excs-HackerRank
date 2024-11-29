num_inicio=int(input('numero: '))
num_final=int(input('numero final: '))
lista_primos=[]
for num in range(num_inicio, num_final+1):
    primo=True
    for n in range(2, num):
        if num%n==0:
            primo=False
            break
    if primo:
        lista_primos.append(num)
print(lista_primos)