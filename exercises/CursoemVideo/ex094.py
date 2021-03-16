lista = []
total = media = 0
while True:
    dicio = {}
    dicio['nome'] = str(input('Nome: '))
    while True:
        dicio['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dicio['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dicio['idade'] = int(input('Idade: '))
    total += dicio['idade']
    lista.append(dicio.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda com apenas S ou N.')
    if continua == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas')
media = total / len(lista)
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')