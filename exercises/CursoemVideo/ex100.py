from random import randint
from time import sleep
def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista} temos {soma}')



def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(1,10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')

teste = []
sorteia(teste)
somapar(teste)