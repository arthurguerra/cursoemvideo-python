from random import randint
from time import sleep
from operator import itemgetter
dicio = {}
alunos = []
for c in range(4):
    dicio['jogador'] = f'jogador{c+1}'
    dicio['número'] = randint(1, 6)
    alunos.append(dicio.copy())
print('Valores encontrados:')
for a in alunos:
    print(f'{a["jogador"]} tirou {a["número"]} no dado.')
print('-=' * 20)
print(' == RANKING DOS JOGADORES == ')
ranking = sorted(alunos, key=itemgetter('número'), reverse=True)
for k, j in enumerate(ranking):
    print(f'    {k+1}º lugar: {j["jogador"]} com {j["número"]}.')