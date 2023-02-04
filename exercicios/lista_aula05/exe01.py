cpfRecebido = input('Digite o CPF: ')

# contagem = len(cpfRecebido)

# if contagem != 11:
#     print('CPF inválido')
# else:
#     print('CPF válido')

# outra forma, usando for para iterar na string
# string = cadeia de caracteres
contador = 0
for numero in cpfRecebido:
    contador += 1

print(contador)

# if contador != 11:
#     print('CPF inválido')
# else:
#     print('CPF válido')