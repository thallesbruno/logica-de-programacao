# is, is not
# int 
# verifica se um valor é igual ao comparado
# Ctrl + K + U comenta
# Ctrl + K + U remove comentário
numero = int(5)
outroNumero = int(5)

numeroFloat = float(3.5)
outroNumeroFloat = float(3.5)

caracteres = 'abc'
outrosCaracteres = 'abc'

print('is int')
print(outroNumero is numero)
print('is float')
print(numeroFloat is outroNumeroFloat)
print('is str')
print(caracteres is outrosCaracteres)

lista = [1, 2, 3]
outraLista = [1, 2, 3]

print('is lista')
print(lista is outraLista)

tupla = (1, 2, 3)
outraTupla = (1, 2, 3)

print('is tupla')
print(tupla is outraTupla)

dicionario = { 1: "asd" }
outroDicionario = { 1: "asd" }

print('is dict')
print(dicionario is outroDicionario)

# tipos primitivos vs tipos built-in

# tupla --> tipo valor
# lista e dict --> tipo referência
    # variável aponta para um lugar na memória
# == vs is