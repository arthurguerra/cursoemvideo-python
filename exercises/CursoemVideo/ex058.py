from random import randint
computador = randint(0, 11)
tentativas = 0
acertou = False
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('Mais...Tente mais uma vez.')
    if jogador > computador:
        print('Menos...Tente mais uma vez.')

print('ACERTOU com {} tentativas. Parabéns!'.format(tentativas))
