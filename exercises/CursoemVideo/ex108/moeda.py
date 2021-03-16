def aumentar(n=0, p=0):
    final = n + (n / 100) * p
    return final


def diminuir(n=0, p=0):
    final = n - (n / 100) * p
    return final


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
