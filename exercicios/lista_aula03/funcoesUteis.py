def funcaoI(n):
    i = 1
    lista = []

    while i <= n:
        lista.append(i)
        print(lista)
        i += 1

def funcaoJ(n):
  #solução com range
    for i in range(n):
        i += 1
        print(f'{str(i) * i}')
    #solução sem range
    # i = 1
    # while i <= n:
    #     print(f'{str(i) * i}')
    #     i += 1

def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

def imprimeLinha(numero):
    for n in range(1, numero + 1):
        print(('  {} ').format(n), end='')
    print()

def imprimeSequencia(numero):
    for numero in range(numero + 1):
        imprimeLinha(numero)

