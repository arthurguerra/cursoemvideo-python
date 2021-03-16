from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
c = 0
while True:
    n = int(input('Diga um valor: '))
    p = ' '
    while p not in 'PpIi':
        p = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(1, 10)
    total = n + pc
    print('-' * 30)
    print(f'Você jogou {n} e o computador {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)
    if p == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            c += 1
        else:
            print('Você PERDEU!!!')
            break
    elif p == 'I':
        if total % 2 != 0:
            print('Você VENCEU!!!')
            c += 1
        else:
            print('Você PERDEU!!!')
            break
    print('Vamos jogar novamente...')
    print('=-' * 20)
print('=-' * 20)
print(f'GAME OVER! Você venceu {c} vezes.')

