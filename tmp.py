# # programa para tentar acessar uym número informado
# numeroCerto = 4

# chuteUm = int(input("Digite o primeiro chute para tentar acertar: "))
# if chuteUm == numeroCerto:
#     print('Acertou!')
# else:
#     print('Errou!')

# chuteDois = int(input("Digite o segundo chute para tentar acertar: "))
# if chuteDois == numeroCerto:
#     print('Acertou!')
# else:
#     print('Errou!')

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')

onix = Carro('Onix')
print(onix.acelerar())