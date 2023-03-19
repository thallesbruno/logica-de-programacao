# # percentuais
# pFaixaUm = 0.075
# pFaixaDois = 0.09
# pFaixaTres = 0.12
# pFaixaQuatro = 0.14
# # faixas salariais
# fSalarialUm = 1302
# fSalarialDois = 1302.01
# fSalarialTres = 2571.29

# # faixasSalariais2023 = (1302, 1302.01, )

# valorINSS = 0.0

# salario = float(input('Entre com o salário: '))

# if salario <= fSalarialUm:  # legibilidade de software
#     valorINSS = salario * pFaixaUm
# elif salario >= fSalarialDois and salario < fSalarialTres:
#     valorINSS = salario * pFaixaDois


# print(f'Valor do INSS: {valorINSS}')
class Inss:
    aliqMinima = 0.075
    aliqMedia = 0.09
    aliqMaxima = 15.0
    salarrio = 0.0

    def __init__(self, salario):
        self.salario = salario

    def defineEnquadramentos(self):
        if self.salario < 1320:
            print(self.salario * 0.075)
        elif self.salario > 1320.01 and self.salario < 2500:
            print(self.salario * 0.09)

i = Inss()
i.defineEnquadramentos()