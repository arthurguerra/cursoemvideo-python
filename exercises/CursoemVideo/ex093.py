dicio = {}
jogos = []
total = 0
dicio['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for c in range(partidas):
    jogos.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += jogos[c]
dicio['gols'] = jogos[:]
dicio['total'] = total
print('-='*20)
print(dicio)
print('-='*20)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dicio["nome"]} jogou {partidas} partidas')
for c in range(len(jogos)):
    print(f'    => Na partida {c+1}, fez {jogos[c]} gols.')
print(f'Foi um total de {total} gols.')
