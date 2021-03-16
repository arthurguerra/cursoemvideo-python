d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(d))
if d <= 200:
    preço = d * 0.5
else:
    preço = d * 0.45
print('E o preço da sua viagem é: R${:.2f}.'.format(preço))