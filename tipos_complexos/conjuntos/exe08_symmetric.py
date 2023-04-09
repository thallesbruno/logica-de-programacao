'''symmetric_difference(): Retorna um novo conjunto que
 contém os elementos presentes em apenas um dos conjuntos.'''

frutas1 = {'banana', 'maçã', 'uva'}
frutas2 = {'abacaxi', 'limão', 'laranja', 'banana', 'uva'}
frutas_diferentes = frutas1.symmetric_difference(frutas2)
print(frutas_diferentes) # saída: {'maçã', 'abacaxi', 'limão', 'laranja'}
