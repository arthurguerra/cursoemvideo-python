def vota(num):
    from datetime import date
    atual = date.today().year
    idade = atual - num
    if idade < 16:
        resp = 'NÃO VOTA'
    elif idade > 65 or 16 <= idade < 18:
        resp = 'VOTO OPCIONAL'
    else:
        resp = 'VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {resp}'


# PROGRAMA PRINCIPAL
while True:
    print('-' * 30)
    ano = int(input('Em que ano você nasceu? '))
    print(vota(ano))
    print('-' * 30)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('VOLTE SEMPRE!')
