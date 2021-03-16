par = []
impar = []
lista = [par, impar]
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
impar.sort()
par.sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')