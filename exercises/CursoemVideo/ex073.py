tabela = 'Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo',\
         'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Corinthians',\
         'Bragantino', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Sport',\
         'Fortaleza', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo'
print('-=' * 20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'O Grêmio está na {tabela.index("Grêmio")+1}ª posicão')
