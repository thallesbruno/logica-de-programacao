#  and, or, not'

dictEfgs = {
    'efg1': 'Luiz Rassi',
    'efg2': 'Sara Kubitscheck',
    'efg3': 'Luiz Bittencourt'
}

if dictEfgs['efg1'] == 'Luiz Rassi':
    print(True)
else:
    print(False)

idade = 18
possuiRg = True

if idade >= 18 or possuiRg is True:
    print('ok')

if dictEfgs['efg1'] == 'Luiz Rassi' and dictEfgs['efg2'] == 'Sarah Kubitscheck':
    print(True)
else:
    print(False)

if dictEfgs['efg1'] == 'Luiz Rassi' or dictEfgs['efg2'] == 'Sarah Kubitscheck':
    print(True)
else:
    print(False)

if dictEfgs['efg2'] == 'Sarah Kubitscheck' or dictEfgs['efg1'] == 'Luiz Rassi':
    print(True)
else:
    print(False)

if not dictEfgs['efg2'] == 'Sarah Kubitscheck':
    # True - 
    print(True)
else:
    print(False)

# diferença entre and e &
# disclaimer
# & - bitwise