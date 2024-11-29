may=0
sim=0
num=0
login=(True)
while (login):
    usuaario=input('Crea un usuario válido: ')
    if len(usuaario) < 8:
        print( 'El nombre de usuario debe contener al menos 8 caracteres')
    if  len(usuaario)>10:
        print('El nombre de usuario no puede contener más de 10 caracteres')
    else:
        for caracter in usuaario:
            if caracter.isalpha():
                may = may+1
            if caracter.isdigit():
                num += 1
            if caracter.isalnum()==False:
                sim += 1
    if may>0 and num>0 and sim == False:
        print('usuario correcto')
    else:
        print('El nombre de usuario puede contener solo letras y números')

