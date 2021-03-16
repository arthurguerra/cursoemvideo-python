a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        t = 'EQUILÁTERO'
    elif a != b != c != a:
        t = 'ESCALENO'
    else:
        t = 'ISÓSCELES'
    print('Os segmentos acima PODEM FORMAR um triângulo {}!'.format(t))
else:
    print('O segmento acima NÃO PODE FORMAR triângulo!')