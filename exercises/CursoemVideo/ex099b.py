from time import sleep


def maior(lista):
    print('-='*20)
    print('Analisando os valores passados...')
    sleep(1)
    print('Valores = ', end='')
    for v in lista:
        print(v, end=' ')
        sleep(0.25)
    print(f'\nForam informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')
    lista.sort()
    print(f'Os valores em ordem crescente são: ', end='')
    for v in lista:
        print(v, end=' ')
    print()
    print('-='*20)

while True:
    valores = []
    tamanho = int(input('Digite quantos valores você quer analisar: '))
    for c in range(tamanho):
        valores.append(int(input(f'Digite o {c+1}º valor: ')))
    maior(valores)

