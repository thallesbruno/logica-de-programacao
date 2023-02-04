sexo = input('Informe o sexo (M para masculino e F para feminino): ')

if sexo == 'M' or sexo == 'm' or sexo == 'masculino' or sexo =='Masculino':
    print('Sexo masculino.')
elif sexo == 'F' or sexo == 'f' or sexo == 'feminino' or sexo == 'feminino':
    print('Sexo feminino.')
else:
    print('Sexo inválido.')