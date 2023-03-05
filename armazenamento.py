# dict = {}

# contador = 1

# while contador <= 5:
#     contador += 1
#     dict[contador] = input('Digite algo: ')

# print('----- Agora vamos imprimir os resultados -----')

contador = 0

# estrutura de repetição => enquanto
# while contador < 5: # enquanto a condição fpor verdadeira, faça...
# print('ok' + str(contador))
# contador += 1

lista = [0, 1, 2, 3, 4, ]

for item in lista:
    print('ok' + str(item))

# continua o código...

sairDoPrograma = ''

while sairDoPrograma != 'SAIR':
    print('executou')

    sairDoPrograma = input('Digite SAIR para sair: ')
