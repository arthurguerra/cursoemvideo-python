lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('-=' * 20)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são: {lista}')
if 5 in lista:
    print(f'Você digitou o valor 5 na posição {lista.index(5) + 1}')
else:
    print('O valor 5 não foi encontrado na lista!')
