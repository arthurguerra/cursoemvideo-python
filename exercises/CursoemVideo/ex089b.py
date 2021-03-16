dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(dados) - 1:
        print(f'Notas de {dados[mostrar][0]} são {dados[mostrar][1]}')
print('<<< Volte Sempre! >>>')
