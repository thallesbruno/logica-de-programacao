listaDeCompras = []
temporaria = ''
sair = ''
CODIGODESAIDA = 999

while sair != 'SAIR':
    temporaria = input('Digite o item ou SAIR: ')

    if temporaria == 'SAIR':
        sair = temporaria
    else:
        listaDeCompras.append(temporaria)

print('\n----- ITENS A COMPRAR (a verificar) -----')
for item in listaDeCompras:  # itera sobre os itens da lista
    print(f'Item: {item}')

codigoItemQueDesejaAlterar = int(
    input('Deseja alterar algum item? Caso sim, digite o código ou 999 para sair: '))

while codigoItemQueDesejaAlterar != CODIGODESAIDA:
    listaDeCompras[codigoItemQueDesejaAlterar] = input(
        'Digite o novo nome do item: ')
    codigoItemQueDesejaAlterar = int(
        input('Digite o código do item ou 999 para sair: '))

listaDeCompras.sort()

print('\n----- ITENS A COMPRAR -----')
print(listaDeCompras)


# for item in listaDeCompras:  # itera sobre os itens da lista
#     print(f'Item: {item}')
