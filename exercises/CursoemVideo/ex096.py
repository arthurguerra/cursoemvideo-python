def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno de  dimensões {larg} x {comp} é de {area}m².')


def lin():
    print('-' * 20)


print(' Controle de Terrenos')
lin()
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
lin()
area(largura, comprimento)


