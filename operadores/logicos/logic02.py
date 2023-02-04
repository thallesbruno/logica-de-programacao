idade = 17
possuiRg = False

# regra para tirar carteira
if idade >= 18 or possuiRg is True:
    print('Pode tirar carteira')
else:
    print('Não pode tirar carteira')
# and => é exclusivo
# or => é inclusivo