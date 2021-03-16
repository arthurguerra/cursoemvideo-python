print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar ?'))
cont = 2
f1 = 0
f2 = 1
print(f1, ' -> ', f2, end=' -> ')
while cont < n:
    f3 = f1 + f2
    print(f3, end=' -> ')
    f1 = f2
    f2 = f3
    cont += 1
print('FIM')
