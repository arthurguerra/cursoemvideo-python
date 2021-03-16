def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    if show:
        for c in range(n, 0, -1):
            f *= c
            if c == n:
                print(c, end=' ')
            else:
                print(f'x {c}', end=' ')
        return f'= {f}'
    else:
        for c in range(n, 0, -1):
            f *= c
        return f


print(fatorial(5))
while True:
    print('-'*30)
    número = int(input('Digite um número para calcular seu fatorial: '))
    while True:
        mostrar = str(input('Gostaria de mostrar a conta? [S/N] ')).strip().upper()[0]
        if mostrar in 'SN':
            break
        print('ERRO!!! Digite apenas SIM ou NÃO!')
    if mostrar == 'S':
        show = True
    else:
        show = False
    print(fatorial(número, show))
    print('-'*30)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
