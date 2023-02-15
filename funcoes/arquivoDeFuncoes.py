def calculadora(operacao, n1, n2):
    if operacao == 1:
        soma = n1 + n2
        print(f'Soma: {soma}')
    elif operacao == 2:
        subtracao = n1 - n2
        print(f'Subtracao: {subtracao}')
    elif operacao == 3:
        multiplicacao = n1 * n2
        print(f'Multiplicação: {multiplicacao}')
    elif operacao == 4:
        divisao = n1 / n2
        print(f'Divisão: {divisao}')

def soma(n1, n2):
    soma = n1 + n2
    return soma

def selecionaOper(operacao):
    if operacao == 1:
        soma()

