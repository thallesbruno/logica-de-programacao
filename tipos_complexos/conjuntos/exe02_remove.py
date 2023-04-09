'''remove(): Remove um elemento do conjunto.
 Se o elemento não existir, uma exceção é lançada.'''
frutas = {'banana', 'maçã', 'uva'}
frutas.remove('banana')
print(frutas) # saída: {'maçã', 'uva'}
