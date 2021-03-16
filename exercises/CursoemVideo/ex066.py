cont = soma = media = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
media = soma / cont
print(f'A soma dos {cont} valores foi {soma} e a media foi {media}!')
