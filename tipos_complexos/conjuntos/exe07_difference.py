'''difference(): Retorna um novo conjunto que
 contém os elementos presentes em um conjunto, mas não em outro.'''

frutas1 = {'banana', 'maçã', 'uva'}
frutas2 = {'abacaxi', 'limão', 'laranja', 'banana', 'uva'}
frutas_diferentes = frutas1.difference(frutas2)
print(frutas_diferentes) # saída: {'maçã'}
