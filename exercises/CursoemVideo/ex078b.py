mai = men = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} na posição: ', end='')
for c in range(0, len(valores)):
    if valores[c] == mai:
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {men} na posiÇão: ', end='')
for c, v in enumerate(valores):
    if v == men:
        print(f'{c}', end='...')