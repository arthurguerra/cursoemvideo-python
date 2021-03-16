print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = a1
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(termo, end=' -> ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
