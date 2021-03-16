from ex107 import moeda


while True:
    p = float(input('Digite o preço: R$ '))
    print('[ 0 ] =========================  AUMENTAR\n'
          '[ 1 ] =========================  DIMINUIR\n'
          '[ 2 ] =========================  DOBRO\n'
          '[ 3 ] =========================  METADE\n'
          '[ 4 ] =========================  DIGITAR UM NOVO PREÇO')
    opção = 5
    while opção != 4:
        opção = int(input('Escolha a operação: [Digite 4 para um novo preço] '))
        if opção == 0:
            aumenta = int(input('Porcentagem que gostaria de adicionar: '))
            print(f'Aumentando {aumenta}% de {p}, temos {moeda.aumentar(p, aumenta)}')
        if opção == 1:
            diminui = int(input('Porcentagem que gostaria de diminuir: '))
            print(f'Reduzindo {diminui}% de {p}, temos {moeda.diminuir(p, diminui)}')
        if opção == 2:
            print(f'O dobro de {p} é {moeda.dobro(p)}')
        if opção == 3:
            print(f'A metade de {p} é {moeda.metade(p)}')
        print('-'*30)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print(' << ENCERRANDO >> ')
