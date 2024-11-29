import math
lista=[1,2,3,4,5,6,7,8,9,10]
lista_fact=[]
fact=[math.factorial(i) for i in lista]
lista_fact.append(fact)
print(lista)
print(lista_fact)