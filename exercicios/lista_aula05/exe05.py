nome = input('Entre com o nome: ')
idade = int(input('Entre com a idade: '))

if idade >= 18:
    print('Olá, %s . Você têm %s de idade e agora pode pagar o lanche!' % (nome, str(idade)))
else:
    print('Olá, %s . Você têm %s de idade e ainda tem que pedir $$ para seu pai!!' % (nome, str(idade)))