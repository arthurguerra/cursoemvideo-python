valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 20)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for c in range(0, len(valores)):
    if valores[c] == max(valores):
        print(f'{c}', end='...')
print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}', end='...')

