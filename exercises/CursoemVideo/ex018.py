import math
a = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(a))
print('O ângulo de {} possui as seguintes propriedades:\nSeno: {:.2f}'.format(a, seno))
cosseno = math.cos(math.radians(a))
print('Cosseno: {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(a))
print('Tangente: {:.2f}'.format(tangente))