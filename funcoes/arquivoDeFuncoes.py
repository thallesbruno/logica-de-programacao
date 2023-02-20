def calculadora(operacao: float, n1: float, n2: float) -> None:
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

def soma(n1: float, n2: float) -> float:
    soma = n1 + n2
    return soma

def divisao(n1: int, n2: int) -> float:
    return n1 / n2

def selecionaOper(operacao) -> bool:
    if operacao == 1:
        soma()
    else:
        return False
