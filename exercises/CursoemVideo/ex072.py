extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco',\
          'seis', 'sete', 'oito', 'nove', 'dez',\
          'onze', 'doze', 'treze', 'catorez', 'quinze',\
          'dezesseis', 'dezessete', 'dezoito', 'dezenovo,', 'vinte'
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente...', end='')
    print(f'Você digitou o número {extenso[n]}')
    while True:
        continua = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break