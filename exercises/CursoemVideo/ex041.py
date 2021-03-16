from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('Classificação: \033[31m{}\033[m.'.format(categoria))


