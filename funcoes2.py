def operacaoMat(numeroUm, numeroDois, tipoDeOperacao):
    if tipoDeOperacao == 'SOM':
        return numeroUm + numeroDois
    elif tipoDeOperacao == 'SUB':
        return numeroUm - numeroDois

operacaoMat(2, 2)
print(soma(3, 3))

resultadoDaSoma = soma(4, 4)
resultadoDeOutraSoma = soma(5, 5)

print(resultadoDaSoma)
print(resultadoDeOutraSoma)
