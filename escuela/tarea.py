texto = input('ingresa una  palabra o frase:  ')
#texto=texto.replace(' ','')

voltear = texto[::-1]
print(voltear)
if voltear ==texto :
    print('la frase es palindromo ')
else:
    print('la frase no es palindromo')

