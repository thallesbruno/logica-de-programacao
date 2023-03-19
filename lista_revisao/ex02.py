contador = 1
while contador <= 5:
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    print(f"""Olá, {nome}.
Você é a pessoa número {contador}
Você pode dirigir: {idade >= 18}""")
    contador += 1

print('Encerrando...')