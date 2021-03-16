cinquenta = vinte = dez = um = 0
print('=' * 40)
print('{:^40}'.format('BANCO ARTHUR'))
print('=' * 40)
valor = int(input('Qual valor você quer sacar? R$'))
cinquenta = valor // 50
valor = valor % 50
vinte = valor // 20
valor = valor % 20
dez = valor // 10
valor = valor % 10
um = valor // 1
if cinquenta != 0:
    print(f'Total de {cinquenta} cédulas de R$50')
if vinte != 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez != 0:
    print(f'Total de {dez} cédulas de R$10')
if um != 0:
    print(f'Total de {um} cédulas de R$1')
print('=' * 40)
print('Volte sempre ao BANCO ARTHUR! Tenha um bom dia!')