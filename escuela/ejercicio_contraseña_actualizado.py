
cadena= 'nombre apellido'
cambio= cadena.replace('nombre apellido', 'Jorge Garcia')
print('cadena sin cambiar: ',cadena)
print('Estimado sr. ',cambio)
print()

### 2 quitar el espacio:
print('quitar el espacio izquierdo: ')
enlace_1= '          www.google.com.mx'
enlace_1_mod=enlace_1.lstrip()
print('cadena sin cambio: ',enlace_1)
print(enlace_1_mod)


print()
# -- 3. Elimina los caracteres en blanco de la siguiente cadena --
print('Elimina los caracteres en blanco de la siguiente cadena: ')
enlace_2 = '     www.google.com.mx    '
enlace_2_cambiado= enlace_2.strip()
print('cadena sin cambios: ',enlace_2)
print(enlace_2_cambiado)
print()

# -- 4. Elimina los caracteres en blanco de la siguiente cadena --
print('Elimina los caracteres en blanco de la siguiente cadena: ')
enlace_3 = 'www.google.com.mx      '
enlace_3_esp= enlace_3.rstrip()
print('texto sin modificar: ',enlace_3)
print(enlace_3_esp)
print()
# -- 5. Convierte la siguiente cadena a lista --
lista_frase = 'Esta es una cadena que voy a convertir a lista'
palabra_list= lista_frase.split()
print('palabra a convertir: ',lista_frase)
print('palabra convertida a lista: ',palabra_list)

# -- 6. Validación de nombres de usuarios. 
# Solicita al usuario que ingrese un nombre de usuario para validarlo
# Dicha validación deberá cumplir con los siguientes criterios de aceptación:
# El nombre de usuario debe contener un mínimo de 8 caracteres y un máximo de 10.
# El nombre de usuario debe ser alfanumérico.
# Nombre de usuario con menos de 8 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
# Nombre de usuario con más de 10 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
# Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
# Nombre de usuario válido, retorna True.

# Valida con los siguientes datos ingresados por el usuario: 
# k4w4m4
# k4w4m4*.
# k4w4m4fria
# k4w4m4fria5
print()
print()
alfabeto=0
caracteres=0
digito=0
usuaario=input('Crea un usuario válido: ')
if len(usuaario) < 8:
    print( 'El nombre de usuario debe contener al menos 8 caracteres')
if  len(usuaario)>10:
    print('El nombre de usuario no puede contener más de 10 caracteres')
else:
    for caracter in usuaario:
        if caracter.isalpha():
            alfabeto += 1
        if caracter.isdigit():
            digito += 1
        if caracter.isalnum()==False:
            caracter += 1
if alfabeto>0 and digito>0 and caracter == False:
    print(True)
else:
    print('El nombre de usuario puede contener solo letras y números')



# -- 7. Valida la contraseña
# Solicita al usuario que registre una contraseña segura
# La validación deberá cumplir con los siguientes criterios de aceptación:
# La contraseña debe contener un mínimo de 8 caracteres.
# La contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
# La contraseña no puede contener espacios en blanco. El Método para saber si la contraseña tiene espacios en blanco o no es isspace()
# Si la contraseña es válida, 
    #   retorna True.
# Si la contraseña es inválida,     
    #   retorna el mensaje "La contraseña elegida no es segura".

# Valida con los siguientes datos ingresados por el usuario: 
# k0nTr4seña
# k0nTr4seña*.
# kontraseña
# 12345678  

# cadena.isdigit() #Muestra si una cadena contiene números
# cadena.islower() #Muestra si una cadena contiene letras mínusculas
# cadena.isupper() #Muestra si una cadena cintiene letras mayúscula
minu=0
mayu=0
simb=0
nume=0
espa=0

print()
contra=input('Crea una contraseña válida: ')
if len(contra) < 8:
    print( 'la contraseña es demasiado corta')
else:
    for caracter in contra:
        print(caracter, end=' ')
        if caracter.islower():
            minu += 1
        if caracter.isupper():
            mayu = mayu+1
        if caracter.isdigit():
            nume += 1
        if caracter.isalnum()==False:
            simb += 1
        if caracter.count(' ')>0:
            espa += 1
        
    print(f'Minusculas: {minu}, mayuscula: {mayu}, numeros: {nume}, simbolo: {simb}, espacios: {espa}')
    print()
    if minu>0 and  mayu>0 and nume>0 and simb>0 and espa==0:
        print(True)
    else:
        print('La contraseña es invalida')

    


# -- 8. Realiza el ejercicio anterior registrando un usuario y contraseña válidos.
        # Si el usuario es inválido, deberá solicitar que vuelva a ingresar un usuario válido, según los mensajes de validación
        # Cuando el usuario sea válido, deberá solicitar el ingreso de una contraseña segura
            # Si la contraseña no es segura, deberá imprimir el mensaje correspondiente y solicitar una nueva contraseña válida

        # Cuando ambos ingresos sean válidos, se visualizará un mensaje con la leyenda:
            # 'Tu usuario registrado es: '
            # 'Tu contraseña registrada es: '

            # ¿Deseas registrar nuevos datos? s/n:
                # Si la respuesta es 's', solicitará nuevamente usuario y contraseña
                # Si la respuesta es 'n', deberá salir del sistema con un mensaje de despedida
                # Si la respuesta es diferente a 's' o a 'n', deberá solicitar que únicamente ingresa 'n' o 's'+
alfabeto=0
digito=0
caracteres=0
minu=0
mayu=0
simb=0
nume=0
espa=0
login=True
while login:
    usua=input('Ingresa un nombre de usuario válido: ')
    if len(usua) >=8 and len(usua)<=10:
        for carac in usua:
            if carac.isalpha():
                alfabeto+=1
            if carac.isdigit():
                digito+=1
            if carac.isalnum()==False:
                caracteres+=1
    if digito>0 and alfabeto>0 and caracteres==False:
        login2=True
        print()
        while login2:
            contra=input('Crea una contraseña válida: ')
            if len(contra) < 8:
                print( 'la contraseña es demasiado corta')
            else:
                for caracter in contra:
                    if caracter.islower():
                        minu += 1
                    if caracter.isupper():
                        mayu =+1
                    if caracter.isdigit():
                        nume += 1
                    if caracter.isalnum()==False:
                        simb += 1
                    if caracter.count(' ')>0:
                        espa += 1
                print()
            if minu>0 and  mayu>0 and nume>0 and simb>0 and espa==0:
                print()
                print(f'''Tu usuario registrado es: {usua}\nTu contraseña registrada es: {contra} ''')
                print()
                entrar=True
                while entrar:
                    decision=input('¿Deseas registrar nuevos datos? s/n: ')
                    if decision=='n':
                        print('Hasta pronto')
                        login=False
                        entrar=False
                    elif decision=='s':
                        entrar=False
                    else:
                        print('Sólo "s" y "n" minuscula')

                login2=False
            else:
                print('La contraseña elegida no es segura')
        #login=False
    elif len(usua) < 8:
        print( 'El nombre de usuario debe contener al menos 8 caracteres')
    elif len(usua)>10:
        print('El nombre de usuario no puede contener más de 10 caracteres')    
    else:    
        print('El nombre de usuario puede contener solo letras y números')




