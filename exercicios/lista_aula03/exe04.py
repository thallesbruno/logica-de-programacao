def positivoNegativo(x):
    # verificação de + ou -
    if x > 0:
        #print('P') -> retorna None
        return 'P'
    elif x == 0:
        return 'NEUTRO'
    else:
        #print('N') -> retorna None
        return 'N'

numeroAComparar = int(input('Digite um valor: '))
retorno = positivoNegativo(numeroAComparar)

print(retorno) # variavel
print(positivoNegativo(numeroAComparar)) # retorno direto