from datetime import date


def voto(idade):
    if idade >= 18:
        if idade >= 65:
            resp = 'VOTO OPCIONAL'
        else:
            resp = 'VOTO OBRIGATÓRIO'
    if idade < 18:
        resp = 'NÃO VOTA'
    return resp


#PROGRAMA PRINCIPAL
atual = date.today().year
while True:
    print('-' * 30)
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    print(f'Com {idade} anos: {voto(idade)}')
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
