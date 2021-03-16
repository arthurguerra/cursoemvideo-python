from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
porc = int(input('Digite a porcentagem que vc gostaria de adicionar: '))
print(f'Aumentando {porc}% de {moeda.moeda(p)}, temos {moeda.aumentar(p, porc, True)}')
diminui = int(input('Digite a porcentagem que vc gostaria de reduiz: '))
print(f'Reduzindo {diminui}% de {moeda.moeda(p)}, temos {moeda.diminuir(p, diminui, True)}')
