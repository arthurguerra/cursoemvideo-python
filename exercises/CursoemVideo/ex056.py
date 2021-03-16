total = 0
velho = 0
menina = 0
for c in range(1,5):
    print('-' * 5, '{}ª PESSOA'.format(c), '-' * 5)
    nome = str(input('Nome: '))
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    total += idade
    if sexo == 'M':
        if idade > velho:
            velho = idade
            velhonome = nome
    if sexo == 'F':
        if idade < 20:
            menina += 1

print('A média de idade do grupo é de {} anos.'.format(total/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, velhonome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menina))