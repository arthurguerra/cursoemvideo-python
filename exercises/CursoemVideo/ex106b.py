cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'azul': '\033[1;44m',
         'vermelho': '\033[1;41m',
         'branco': '\033[7;29m'}


def ajuda(com):
    from time import sleep
    título(f"Acessando o manual do comando '{com}'", 'azul')
    sleep(1)
    print(cores['branco'], end='')
    help(com)
    print(cores['limpa'], end='')
    sleep(1)


def título(msg, cor='limpa'):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cores['limpa'], end='')


# PROGRAMA PRINCIPAL
while True:
    título('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 'vermelho')
