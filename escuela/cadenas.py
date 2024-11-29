cadena = 'abcdefghijklmnñopqrstuvwxyz'
print('capitalize: ', cadena.capitalize()) # cambia la escritura del texto a tipo oracion

print('uper: ', cadena.upper()) # cambia el texto a mayuscula

print('lower: ', cadena.lower()) # cambia el texto a minuscula

print('tamaño de la cadena: ', len(cadena)) # muestra la longitud de  la cadena

print('es alfa numerico: ', cadena.isalnum()) #muestra si una cadena contiene caracteres alfanumerico numeros y letras y tiene al menos un caracter

print('es numero?: ', cadena.isalpha())# muestra si una cadena contiene letras del alfabeto

print('es numero?: ', cadena.isdigit()) #muestra si la caena tiene digito

print('es minuscula:', cadena.islower())# muestra si tien letras minuscula

print('es mayuscula:', cadena.isupper()) #muestra si tiene letra mayuscula

#max y min
cadena3='bcdefzjk'
print('letra menor: ' , min(cadena3))
print('letra mayor: ' , max(cadena3))

print('cambia caracter: ', cadena.replace('e','g')) #remplaza caracteres
print('invierte la cadena: ', cadena.swapcase()) # invierte la mayuscula a minusculas y vicervesa

print('conbviertir en lista la cadena: ', cadena.split())
fecha='18.05.2023.hola'
print('separador: ' , fecha.split("."))
cadena1 = '   -.-.     atencion1'
print(cadena1.lstrip('')) # elimina caracteres al comienzo

cadena1= 'atencion2   '
cadena2 = 'hola'
#Elimina caracteres al final de la cadena
print(cadena1.rstrip(), end =  ' ')
print(cadena2)

#elimina caracteres al principio y al final de la cadena
cadena1= '   hola a todos     '
cadena2='loquitos'
print(cadena1.strip(), end =  ' ')
print(cadena2)
#isspace() saber si tiene espacios en blanco o no   