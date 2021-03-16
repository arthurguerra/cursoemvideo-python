from math import sqrt
número = float(input('Digite o número que gostaria de saber a raiz quadrada: '))
raiz = sqrt(número)
cores = {'vermelho':'\033[;31m', 'azul':'\033[;33m', 'limpa':'\033[m'}
print('A raiz quadrada de {}{}{} é {}{}{}!'.format(cores['azul'], número, cores['limpa'], cores['vermelho'], raiz, cores['limpa']))

