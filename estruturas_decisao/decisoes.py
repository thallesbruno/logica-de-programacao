# if 5 > 5:
#     print("5 é maior que 2")
# else:
#     print('erro')

numero = int(input('Digite um número qualquer: '))
if numero > 10: # se numero for maior que 10
    print('Maior que 10')
elif numero > 5: # senão, se numero for maior que 5
    print('Maior que 5 e menor que 10')
elif numero < 5 & numero > 1: # senão, se numero for menor que 5 E numero for maior que 1
    print('Menor que 5 e maior que 1')
else: # senão
    print(f'Menor que 1{numero}')
    print(numero)
    print('ok')
    print('ok')
    print('ok')
    print('ok')
    print('ok')
    print('agora acabou!')

# condicao = True
# if condicao:
#     print('é verdade')

# print('#' * 5 + ' Teste uma variável ' + '#' * 5)
# tentativas = 5
# while tentativas > 0:
#     # print(f"Tentativa: {tentativas}")
#     aposta = int(input('Digite sua aposta: '))

#     if aposta == 10:
#         print("Acertou!")
#         break
#     else:
#         tentativas = tentativas - 1

#     print(f'Tente novamente! Você tem {tentativas} tentativas!')
#     print('-'*10)