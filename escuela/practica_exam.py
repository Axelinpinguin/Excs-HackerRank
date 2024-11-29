letrasvu=0
numerosvu=0
simbolosvu=0
contraseñavalidacion=False
usuariovalidacion=False
validaciones=True

minusculasvc = 0
mayusculasvc = 0
simbolosvc = 0
numerosvc =0
espaciosvc = 0
while (validaciones):
    if usuariovalidacion==False:
        usuarionuevo =input('Ingresa tu usuario: ')
        if  len(usuarionuevo) >= 8 and len (usuarionuevo) <=10:
            for caracteres in usuarionuevo:
                if caracteres.isalpha():
                 letrasvu += 1
                if caracteres.isdigit():
                 numerosvu +=1
                if caracteres.isalnum()==False:
                 simbolosvu +=1
        if numerosvu >0 and letrasvu >0 and simbolosvu ==False :
            usuariovalidacion=True
    if contraseñavalidacion==False:
        contraseñanueva = input('Registra una contraseña valida: ' )
        if len(contraseñanueva) <8 :
            print('La contraseña debe contener al menos 8 caracteres')
        else: 
            for caracteres in contraseñanueva:
                if caracteres. islower():
                   minusculasvc += 1
                if caracteres.isupper():
                   mayusculasvc = mayusculasvc +1
                if caracteres.isdigit():
                  numerosvc += 1  
                if caracteres.isalnum()==False:
                   simbolosvc +=  1
                if caracteres.count(' ') >0:
                 espaciosvc +=1    
        if minusculasvc > 0 and mayusculasvc >0 and numerosvc >0 and simbolosvc >0 and espaciosvc ==0:
           contraseñavalidacion=True
    if usuariovalidacion== True and contraseñavalidacion==True:
       print('tu usuario registrado es: ', usuarionuevo ,'tu contraseña registrada es: ', contraseñanueva)
    opcion= input('¿Desea agregar datos nuevos? s//n')
    while opcion.upper() !='N' and opcion.upper() !='S':
        if opcion.upper()=='S':
             usuariovalidacion=False
             contraseñavalidacion=False
        elif opcion.upper() == 'N':
             validaciones=False
        else:
             print('La opcion no es valida, solo agregue *S* o *N*')