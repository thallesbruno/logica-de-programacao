# atribuição de variáveis
cidade = "Aparecida de Goiânia"
bairro = 'Buriti Sereno'

# aspas triplas - usadas para texto em várias linhas
print(f"""EFG - 
Luis
Rassi
Escola Do Futuro
Situada em {cidade} no {bairro}""")
print('-' * 10)  # separação de código

# aspas triplas
print('''Teste
de
aspas simples''')
print('-' * 10)  # separação de código

# usando aspas siumples para usar aspas duplas dentro da string
print('"Escola do Futuro" Luiz Rassi')
# usando barra invertida para permitir aspas duplas dentro de uma string
print("\"Escola do Futuro\" Luiz Rassi")
# usando aspas triplas
print("""'EFG' - "Luiz Rassi" - Aparecida de Goiânia - 'Buriti Sereno'""")
print('-' * 10)  # separação de código

# pular de linha
print("""Ementa do Curso - "Qualificação em Programação de Computadores":
Lógica de Programação \nSistemas de Computação
Python Básico
Python Intermediário \nOrientação a Objetos
Matemática Discreta
Carga horária: '240 horas'""")
print('-' * 10)  # separação de código

# interpolação de stringss
nome = "Thalles Santos"
empresa = 'EFG Luiz Rassi'.upper()
qtde_funcionarios = 100
mediaMensalidade = 0.00
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
