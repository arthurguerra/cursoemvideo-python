from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('Suas opções: \n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('JOGADA INVÁLIDA!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-='*10)
    print('Computador jogou {}.'.format(itens[pc]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*10)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif pc ==1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
else:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')



