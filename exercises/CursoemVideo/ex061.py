print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 0
while cont < 10:
    print(a1, end=' -> ')
    a1 += razão
    cont += 1
print('FIM')
