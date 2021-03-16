lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print('-=' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

