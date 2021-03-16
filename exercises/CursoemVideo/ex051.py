print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
a1 = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = a1 + (10 - 1) * razão
for c in range(a1, décimo + razão, razão):
    print(a1, end=' -> ')
    a1 += razão
print('ACABOU!')