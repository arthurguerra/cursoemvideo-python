lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
lista.sort()
print('=-' * 20)
print(f'Você digitou os valores: {lista}')