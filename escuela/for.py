print('personajes por ti')
juegoMario =['Mario', 'Luigi', 'peach', 'Bowser', 'yoshi']
print(juegoMario)
print(juegoMario[0])
print(juegoMario[1])
print(juegoMario[2])
print(juegoMario[3])
print(juegoMario[4])
print()
agregar = True
while(agregar):
    nuevopersonaje = input('Escribe otro personaje de MarioBros: ')
    juegoMario.append(nuevopersonaje)
    opc = input('¿quieres seguir agregando personaje? s/n:  ')
    if opc.upper()== 'N':
        agregar = False
    
for nombres_de_personajes in range(0,len(juegoMario)):
    print(f'{nombres_de_personajes+1}. Animo  {juegoMario[nombres_de_personajes]}')
print(juegoMario)
