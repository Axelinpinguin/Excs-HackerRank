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
        # 
    elif len(usua) < 8:
        print( 'El nombre de usuario debe contener al menos 8 caracteres')
    elif len(usua)>10:
        print('El nombre de usuario no puede contener más de 10 caracteres')    
    else:    
        print('El nombre de usuario puede contener solo letras y números')