import math
import sys

a = float(input())
b = float(input())
c = float(input())
delta = float((b * b) - (4 * a * c))
print(delta)
raiz = float(math.sqrt(delta))

if delta < 0 or b % raiz == 0:
    print("Impossivel calcular")
    sys.exit()
else:
    bask1 = ((-(b)) + raiz) / (2 * a)
    bask2 = ((-(b)) - raiz) / (2 * a)
    print(f'R1 = :.2f{bask1}')
    print(f'R2 = :.2f{bask2}')  