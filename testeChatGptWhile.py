itens_de_compras = []

while True:
    item = input("Digite o próximo item da lista de compras (ou 'fim' para encerrar): ")
    if item.lower() == "fim":
        break
    else:
        itens_de_compras.append(item)

print("Lista de compras:")
for item in itens_de_compras:
    print("- " + item)