from random import randint
from time import sleep


def sorteia(lista, tamanho):
    print(f'Sorteando {tamanho} valores para a lista: ', end='')
    for c in range(tamanho):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista} temos {soma}!')


while True:
    lista = []
    tamanho = int(input('Quantos valores você quer sortear? '))
    sorteia(lista, tamanho)
    somapar(lista)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('ENCERRANDO...')
