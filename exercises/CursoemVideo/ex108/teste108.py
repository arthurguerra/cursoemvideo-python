from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
porc = int(input('Digite a porcentagem que vc gostaria de adicionar: '))
print(f'Aumentando {porc}%, temos {moeda.moeda(moeda.aumentar(p, porc))}')
diminui = int(input('Digite a porcentagem que vc gostaria de reduiz: '))
print(f'Reduzindo {diminui}% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.diminuir(p, diminui))}')


