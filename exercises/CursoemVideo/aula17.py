valores = []
quantidade = int(input('Quantos valores você quer? '))
for c in range(0, quantidade):
    valores.append(input('Digite um valor: '))
for c, v in enumerate(valores):
    print(f'Na posição {c+1} você digitou o valor {v}!')
print('Cheguei ao final da lista.')
while True:
    while True:
        resp = str(input('Você quer adicionar mais valores? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
    else:
        adicionar = int(input('Quantos valores vc quer adicionar? '))
    for c in range(0, adicionar):
        valores.append(input('Digite um valor para adicionar: '))
    print(f'Sua lista está com {len(valores)} termos, sendo eles: ', end='')
    for c in valores:
        print(f'{c} ', end='')
    print('\n', end='')


