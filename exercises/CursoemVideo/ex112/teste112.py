from ex112.utilidadesCEV import moeda
from ex112.utilidadesCEV import dado


p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)