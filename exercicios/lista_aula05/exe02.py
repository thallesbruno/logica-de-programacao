nome = input('Entre com o nome: ')
idade = int(input('Entre com a idade: '))

cumprimentoComPercentual = ('Olá, me chamo %s e tenho %s anos de idade.' % (nome, idade))
cumprimentoComFStrings = f'Olá, me chamo {nome} e tenho {idade} anos de idade.'

print(cumprimentoComPercentual)