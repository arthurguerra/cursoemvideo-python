n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', c, '\033[m', end='')
        cont += 1
    else:
        print('\033[31m', c, '\033[m', end='')
if cont == 2:
    print('\nO número {} foi dividido {} vezes\nE por isso ele é PRIMO!'.format(n, cont))
elif cont != 2:
    print('\nO número {} foi dividido {} vezes\nE por isso ele NÃO É PRIMO!'.format(n, cont))