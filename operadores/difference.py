print('- -' * 10)

a = 14
b = 4
 
print(b and a)  # avaliação lógica dos operandos
print(b & a)  # operação AND bit a bit no resultado das expressões

print('- -' * 10)

a1 = 9 # 1001
b1 = 10 # 1010
print(a1 & b1)  # line 1
print(a1 and b1)  # line 2

print('- -' * 10)

a2 = 100
b2 = 200

print(a2 < b2 and b2 > a2)
print(a2 < b2 & b2 > a2)

print('Outro teste: ')

print(a2 < b2 and b2 < a2)
print(a2 < b2 & b2 < a2)

print('- -' * 10)

print(bool(a2))
print(bool(0))