'''crear un programa donde le pidas al usuario 2 calficaciones de esas calificaiones
promediarlo y 
1) si su promedio es igual que 7 que imprima un mensaje de felicidades pero que tiene que mejorar***
2) si su promedio es menor que 7 que imprima un mensaje que diga reprobaste intenta de nuevo***
3) si su calificacion es mayor a 7 que diga felicidades***
4) si su calificacion es mayor de 10 entonces que imprima no existe esta calificacion***'''

note_1=float(input('Enter note: '))
note_2=float(input('Next note: '))
promedium=((note_1+note_2)/2)
print(promedium)
if promedium==7:
    print('Congratulations but you must improve')
elif promedium<7:
    print('You failed try again')
elif promedium>10:
    print('this note does not exist')
elif promedium>7:
    print('Congratulations')