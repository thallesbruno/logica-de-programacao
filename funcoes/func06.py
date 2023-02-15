import sys
import arquivoDeFuncoes as funcoes # importação / alias


print('Entrando na calculadora...')
print('1 => Soma')
print('2 => Subtração')
print('3 => Multiplicação')
print('4 => Divisão')
operacao = int(input('Digite a operação desejada: '))

if operacao > 4:
    print('Digite uma opcão válida!')
    sys.exit()

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

funcoes.calculadora(operacao, n1, n2)