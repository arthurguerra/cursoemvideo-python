def leiaInt(msg):
    núm = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            núm = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return núm



n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')