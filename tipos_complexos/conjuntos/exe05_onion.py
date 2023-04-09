'''union(): Retorna um novo conjunto 
que contém todos os elementos de dois ou mais conjuntos.'''

frutas1 = {'banana', 'maçã', 'uva'}
frutas2 = {'abacaxi', 'limão', 'laranja'}
todas_as_frutas = frutas1.union(frutas2)
print(todas_as_frutas) # saída: {'banana', 'maçã', 'uva', 'abacaxi', 'limão', 'laranja'}
