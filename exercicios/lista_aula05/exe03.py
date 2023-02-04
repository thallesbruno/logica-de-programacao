salarioBruto = float(input('Digite seu salário bruto: '))
PERCENTUAL_FGTS = 0.8

salarioDescontado = salarioBruto * PERCENTUAL_FGTS

print('Salário líquido: %s' % salarioDescontado)
print(f'Salário líquido: {salarioDescontado}')


