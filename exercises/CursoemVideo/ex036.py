valor = float(input('Valor da casa: R$'))
salário = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação será de: R${:.2f}'.format(prest))
if prest > salário*30/100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')