c = total = n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        total += n
        c += 1
print('Você digitou {} número e a soma entre eles foi {}!'.format(c, total))