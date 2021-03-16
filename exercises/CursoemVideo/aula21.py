'''def fatorial(num=1):
    """
    FATORIAL
    :param num: Fatorial a ser descoberto
    :return: Resultado do fatorial de (num)
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f'''


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


número = int(input('Digite um número: '))
if par(número):
    print(f'O número {número} é PAR!')
else:
    print(f'O número {número} é ')
