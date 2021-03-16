from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
chute = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if chute == n:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print('GANHEI, eu pensei no número {} e não no {}!'.format(n, chute))
