#Pedimos al usuario que ingrese las calificaciones
calificaciones = []
while True:
    calificacion = input("Ingrese una calificación (o 'fin' para terminar): ")
    if calificacion.lower() == 'fin':
        break
    calificaciones.append(float(calificacion))

# Calculamos la promedia
promedia = sum(calificaciones) / len(calificaciones)

# Mostramos el resultado
print("La promedia de las calificaciones es:", promedia)