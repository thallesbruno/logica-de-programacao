'''discard(): Remove um elemento do conjunto,
 mas não lança exceção se o elemento não existir.'''

frutas = {'banana', 'maçã', 'uva'}
fruta = frutas.pop()
print(fruta) # saída: 'banana'
print(frutas) # saída: {'maçã', 'uva'}