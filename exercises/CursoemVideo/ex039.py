from datetime import date
atual = date.today().year
sexo = str(input('Qual é o seu sexo? M para masculino e F para feminino? ')).strip()
if sexo.upper() == 'F':
    print('Você não precisa se alistar!')
else:

    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(18 - idade + date.today().year))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos atrás.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(ano + 18))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')



