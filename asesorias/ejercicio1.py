import os
fiel=True
nombre=input('Escribe tu nombre: ')
while fiel:
    nombre_oracion=nombre.capitalize()
    pregunta=input(f' \n¿{nombre_oracion} eres fiel?:\n ')
    if pregunta.lower()=="si":
        os.system('cls')
        print('\n¡ja! hasta crees, intenta de nuevo\n')
    elif pregunta.lower()=="no":
        os.system('cls')
        print('\nLO SABIA, INFIEL\n')
        fiel=False
    else:
        os.system('cls')
        print('Solo puedes responder afirmando o negando')