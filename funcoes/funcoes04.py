print('Entrando na calculadora...')
print('1 => Soma')
print('2 => Subtração')
print('3 => Multiplicação')
print('4 => Divisão')
operacao = int(input('Digite a operação desejada: '))

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if operacao > 4:
    print('Escolha uma opção válida!')
    exit()
# calculos / decisão / mostra do resultado

if operacao == 1:
    soma(n1, n2)
elif operacao == 2:
    subtracao(n1, n2)
elif operacao == 3:
    multiplicacao = n1 * n2
    print(f'Multiplicação: {multiplicacao}')
elif operacao == 2:
    divisao = n1 / n2
    print(f'Divisão: {divisao}')
else:
    print('Digite uma opcão válida!')

