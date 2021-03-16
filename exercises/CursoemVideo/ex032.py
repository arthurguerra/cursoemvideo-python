n = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
b = n % 4
b2 = n % 400
atual = 2021
if n == 0:
    print('O ano de {} NÃO é BISSEXTO!'.format(atual))
    exit()
if b2 == 0:
    print('O ano {} é BISSEXTO!'.format(n))
    exit()
if b == 0:
    print('O ano {} é BISSEXTO!'.format(n))
    exit()
else:
    print('O ano {} NÃO É BISSEXTO!'.format(n))



