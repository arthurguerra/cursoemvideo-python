def leiaInt(msg):
    while True:
        n = str(input(msg))
        try:
            int(n)
            break
        except Exception as erro:
            print('\033[1;31mErro: por favor, digite um número inteiro válido.\033[m')
    return int(n)


def leiaFloat(msg):
    while True:
        n = str(input(msg))
        if n.strip() == '':
            n = 0
        try:
            float(n)
            break
        except:
            print('ERRO: por favor, digite um número real válido.')
    return float(n)


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Didige um número Real:')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')