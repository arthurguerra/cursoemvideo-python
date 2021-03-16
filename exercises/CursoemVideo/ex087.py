matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maiorseg = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
print('-=' * 20)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
        if coluna == 2:
            terceira += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0 or matriz[linha][coluna] > maiorseg:
                maiorseg = matriz[linha][coluna]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maiorseg}.')