from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA')
    opção = int(input('>>>> Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        if n1 < n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
        else:
            print('Os dois números são iguais.')
    elif opção == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida, tente novamente!')
    print('=-=' * 10)
sleep(2)
print('Fim do programa! Volte Sempre!')

