from random import randint
from time import sleep
jogo = {}
for c in range(4):
    jogo[f'jogador{c+1}'] = randint(1, 6)
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=lambda k: k[1], reverse=True)
print('-=' * 20)
print('  == Ranking dos Jogadores: == ')
for k, j in enumerate(ranking):
    print(f'    {k+1}º lugar: {j[0]} com {j[1]}')
    sleep(1)