total = caro = barato = 0
baratoP = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if barato == 0 or preço < barato:
        barato = preço
        baratoP = produto
    if preço > 1000:
        caro += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baratoP} que custa R${barato:.2f}')