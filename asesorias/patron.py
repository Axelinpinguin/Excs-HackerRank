def search(cadena_texto,patron):
    login = False
    rango = len(cadena_texto)-len(patron) # 12 - 3 = 9

    for i in range(0,rango+1): # 9
        if cadena_texto[i:i+len(patron)]==patron: # [1:1+3]=[r:rog]
            login = True
            break

    if login:
        return True
    else:
        return False
    
cadena_texto = 'programacion'
patron = input('Ingrese un patron dentro del texto: ')
#damos valor a la definción
rest=search(cadena_texto,patron)
#imprimimos la definición
print(rest)