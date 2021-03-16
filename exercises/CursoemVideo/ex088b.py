from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer sortear? '))
for c in range(0, quant):
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(f'Sorteando {quant} jogos')
for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
print(f'{"BOA SORTE!":=^30}')