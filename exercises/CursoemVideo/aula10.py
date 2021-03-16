n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m > 6.0:
    print('PARABÉNS!')
else:
    print('ESTUDE MAIS!')