def leiaInt(num):
    while True:
        teste = input(num)
        if teste.isnumeric():
            teste = int(teste)
            return teste
            break
        else:
            print('\033[0;31mERRO! digite um número inteiro válido.\033[m')


# PROGRAMA PRINCIPAL
n = leiaInt('Digite umm número: ')
print(f'Você acabou de digitar o número {n}')
