def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido!!!\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[31mERRO: digite um número Real válido!!!\033[m')
        else:
            return n


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O número inteiro digitado foi {inteiro} e o real foi {real}')