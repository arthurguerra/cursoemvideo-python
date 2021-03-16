from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...\nValores =', end=' ')
    for v in num:
        print(v, end=' ')
        sleep(0.25)
        cont += 1
        if cont == 0:
            maior = v
        if v > maior:
            maior = v
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()