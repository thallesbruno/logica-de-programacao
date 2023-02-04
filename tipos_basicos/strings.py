import datetime

palavra = 'escola'
frase = 'Escola do Futuro Luiz Rassi'
caractere = "F"

#print(type(caractere))

#concatenação de strings (string interpolation)
#f-strings
nome = 'Thalles'
titulo = 'professor'
print(f'Olá, {titulo} {nome}.')

a = 5
b = 3
print(f'A soma de {a} com {b} é igual a {a + b}.')

#%-formatting
print("%s %s" %('Este é um', 'TESTE',))

nome = 'João'
sobrenome = 'Neves'
data = datetime.datetime.now()
print("Olá, %s %s, hoje é %s" %(nome, sobrenome, data,))
print('Olá, %(nome)s %(sobrenome)s, hoje é %(data)s' %(nome, sobrenome, data))

#