def aumentar(n=0, por=0, format=False):
    """
    ->Calcule o aumento de um determinado valor,
    retornando o resultado formatado ou não.
    :param n: O valor a ser reajustado.
    :param por: Porcentagem do aumento.
    :param format: (opcional) Mostra o valor formatado
    :return: O valor reajustado após o aumento.
    """
    final = n + (n / 100) * por
    if format:
        final = moeda(final)
    return final


def diminuir(n=0, por=0, format=False):
    final = n - (n / 100) * por
    return final if not format else moeda(final)


def dobro(n=0, format=False):
    """
    -> Calcula o dobro de um valor n,
    retornando o valor formatado ou não.
    :param n: O valor a ser reajustado
    :param format: (opcional) formatar ou não.
    :return:retorna o dobro de um valor n,
    com ou sem formatação.
    """
    res = n * 2
    return res if not format else moeda(res)


def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')



def resumo(p=0, a=0, d=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço Analisado:":<20} {moeda(p)}')
    print(f'{"Dobro do preço:":<20} {dobro(p, True)}')
    print(f'{"Metade do preço:":<20} {metade(p, True)}')
    print(f'{a}{"% de aumento:":<18} {aumentar(p, a, True)}')
    print(f'{d}{"% de redução:":<18} {diminuir(p, d, True)}')
    print('-'*30)
