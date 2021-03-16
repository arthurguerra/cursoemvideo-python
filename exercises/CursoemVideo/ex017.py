import math
c1 = float(input('Cateto Oposto: '))
c2 = float(input('Cateto Adjacente: '))
h = math.sqrt(pow(c1, 2) + pow(c2, 2))
print('O valor do comprimeto da hipotenusa para um triângulo de catetos {} e {} é {:.2f}'.format(c1, c2, h))
