'''intersection(): Retorna um novo conjunto que contém 
apenas os elementos que estão presentes em dois ou mais conjuntos.'''

frutas1 = {'banana', 'maçã', 'uva'}
frutas2 = {'abacaxi', 'limão', 'laranja', 'banana', 'uva'}
frutas_comuns = frutas1.intersection(frutas2)
print(frutas_comuns) # saída: {'banana', 'uva'}
