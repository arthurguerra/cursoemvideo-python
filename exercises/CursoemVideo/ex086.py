matriz = [[], [], []]
for c in range(0, 3):
    linha0 = matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    linha1 = matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    linha2 = matriz[2]. append(int(input(f'Digite um valor para [2, {c}]: ')))
for c in range(0, len(matriz[0])):
    print(f'[  {matriz[0][c]}  ]', end='')
print()
for c in range(0, len(matriz[1])):
    print(f'[  {matriz[1][c]}  ]', end='')
print()
for c in range(0, len(matriz[2])):
    print(f'[  {matriz[2][c]}  ]', end='')
