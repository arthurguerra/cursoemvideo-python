time = []
while True:
    jogador = {}
    partidas = []
    print('-'*30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(jogos):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Digie apenas S ou N.')
    if continua == 'N':
        break
print('-='*30)
print(f'{"cod":<5}', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador com código {mostrar}! Tente Novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"]}:')
        for k, v in enumerate(time[mostrar]["gols"]):
            print(f'    No jogo {k+1} fez {v} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
