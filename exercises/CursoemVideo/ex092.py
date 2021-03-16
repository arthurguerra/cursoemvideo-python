from datetime import date
dicio = {}
atual = date.today().year
dicio['NOME'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dicio['IDADE'] = atual - nasc
dicio['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicio['CTPS'] != 0:
    dicio['CONTRATAÇÃO'] = int(input('Ano de Contratação: '))
    dicio['SALÁRIO'] = int(input('Salário: R$'))
    aposentadoria = dicio['CONTRATAÇÃO'] - nasc + 35
    dicio['APOSENTADORIA'] = aposentadoria
print('-='*20)
for k, v in dicio.items():
    print(f'  - {k} tem o valor {v}')