a = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {a}')
print(f'O número 9 apareceu {a.count(9)} vezes')
if a.count(3) != 0:
    print(f'O valor 3 apareceu na {a.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for count in a:
    if count % 2 == 0:
        print(count, end=' ')