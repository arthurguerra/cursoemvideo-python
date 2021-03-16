from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if atual - ano >= 18:
        maior += 1
    elif atual - ano < 18:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE tivemos {} pessoas menores de idade'.format(maior, menor))

