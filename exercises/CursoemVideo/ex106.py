from time import sleep


def texto(msg, cor):
    tam = len(msg) + 4
    print(f'{cor}~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    cor = cores['limpa']
    print(cor, end='')


cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'azul': '\033[1;44m',
         'vermelho': '\033[1;41m',
         'branco': '\033[1;46m'}
while True:
    texto('SISTEMA DE AJUDA PyHELP', cores['verde'])
    user = str(input('Função ou Biblioteca > '))
    if user.upper() == 'FIM':
        texto('ATÉ LOGO!', cores['vermelho'])
        break
    texto(f"Acessando o manual do comando '{user}'", cores['azul'])
    sleep(1)
    print(cores['branco'], end='')
    help(user)


