print('-=-' * 20)
print('Analisador de Triângulos: ')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
    t = 'PODEM'
else:
    t = 'NÃO PODEM'
print('Os segmentos acima {} formar triângulo!'.format(t))