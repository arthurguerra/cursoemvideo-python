print('{:=^40}'.format('\033[31m'' LOJAS GUERRA ''\033[m'))
valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opção = int(input('Qual é a sua opção? '))
if opção == 1:
    final = valor - (valor * 10/100)
elif opção == 2:
    final = valor - (valor * 5/100)
elif opção == 3:
    final = valor
    parcelas = final / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcelas))
elif opção == 4:
    vezes = int(input('Quantas parcelas? '))
    final = valor + (valor * 20/100)
    parcelas = final / vezes
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(vezes, parcelas))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
    exit()
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, final))
