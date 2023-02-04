condicao = True

if condicao:
    # o que deve ser feito se a condição for Verdadeira
    print('verdadeiro')
else:
    # o que deve ser feito se a condição for Falsa
    print('falso')

print('-'*20)

numeroCerto = 4
chuteUm = int(input("Digite o primeiro chute para tentar acertar: "))

if chuteUm == numeroCerto:
    print('Acertou!')
else:
    print('Errou!')

chuteDois = int(input("Digite o segundo chute para tentar acertar: "))
if chuteDois == numeroCerto:
    print('Acertou!')
else:
    print('Errou!')
