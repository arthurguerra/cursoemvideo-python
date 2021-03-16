def aumentar(n=0, p=0, format=False):
    final = n + (n / 100) * p
    if format:
        final = moeda(final)
    return final


def diminuir(n=0, p=0, format=False):
    final = n - (n / 100) * p
    return final if not format else moeda(final)


def dobro(n=0, format=False):
    res = n * 2
    return res if not format else moeda(res)


def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
