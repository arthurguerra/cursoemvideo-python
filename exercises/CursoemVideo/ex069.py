maiores = homem = mulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 20)
    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
            mulher += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
            break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')