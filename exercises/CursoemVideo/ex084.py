dado = []
pessoas = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('-=' * 20)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
for c, p in enumerate(pessoas):
    if c == 0:
        maior = menor = p[1]
    elif p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end='...')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end='...')