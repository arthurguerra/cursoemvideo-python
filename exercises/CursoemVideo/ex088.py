from random import randint
from time import sleep
jogos = []
temp = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
while True:
    quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
    if quantidade < 1 or quantidade > 10:
        print('MÁXIMO de 10 jogos, tente novamente...')
    else:
        break
for c in range(0, quantidade):
    for j in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in temp:
                break
        temp.append(n)
    jogos.append(temp[:])
    temp.clear()
print(f'{f"SORTEANDO {quantidade} JOGOS":=^30}')
for j in range(0, len(jogos)):
    jogos[j].sort()
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
print(f'{"< BOA SORTE! >":=^30}')