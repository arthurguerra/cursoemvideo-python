número = int(input('Me diga um número qualquer:'))
resultado = número % 2
if resultado == 1:
    print('O número {} é ÍMPAR!'.format(número))
else:
    print('O número {} é PAR!'.format(número))