from time import sleep


def lin():
    print('-=' * 20)


def contador(início, fim, passo):
    lin()
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -(passo)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(1)
    if início < fim:
        cont = início
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.25)
            cont += passo
        print('FIM!')
    if início > fim:
        cont = início
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.25)
            cont -= passo
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
while True:
    lin()
    print('Agora é sua vez de personalizar a contagem!')
    início = int(input('Início: '))
    fim = int(input('Fim:    '))
    passo = int(input('Passo:  '))
    contador(início, fim, passo )
    lin()
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print(' << ENCERRANDO... VOLTE SEMPRE! >> ')