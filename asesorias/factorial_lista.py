lista=[1,2,3,4,5,6,7,8,9,10]
lista_fact=[]
multiplicador=1
for i in lista:
    multiplicador*=i
    lista_fact.append(multiplicador)
    print(f'El factorial de {i}! = {multiplicador}')
print(f'En formato de lista     = {lista_fact}')    