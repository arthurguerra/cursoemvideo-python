resp = ''
cont = maior = menor = total = media = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    total += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ').strip()[0])
media = total / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi de {} e o menor foi {}'.format(maior, menor))
