soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Dos 6 valores informados, {} são pares e a sua soma é {}'.format(cont, soma))


