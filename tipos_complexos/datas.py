import datetime as classeDeDatas

nome = 'João'
sobrenome = 'Neves'
data = classeDeDatas.datetime.now()
print("Olá, %s %s, hoje é %s" %(nome, sobrenome, data,))

print(f'\n##### UM POUCO DE DATAS #####')
dataFormatada = classeDeDatas.datetime(2023, 1, 16)
print(f'Data informada: {dataFormatada}')

print(f'Mês: {data.strftime("%B")}')
print(f'Mês (número): {data.strftime("%m")}')
print(f'Ano: {data.strftime("%Y")}')
print(f'Dia da semana: {data.strftime("%A")}')

