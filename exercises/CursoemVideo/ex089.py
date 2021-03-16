alunos = []
nomes = []
notas = []
tempnotas = []
medias = []
while True:
    nomes.append(str(input('Nome: ')))
    somanotas = 0
    for c in range(2):
        tempnotas.append(float(input(f'Nota {c+1}: ')))
        somanotas += tempnotas[c]
    medias.append(somanotas / 2)
    notas.append(tempnotas[:])
    tempnotas.clear()
    while True:
        continua = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
alunos.append(nomes[:])
alunos.append(notas[:])
print('-=' * 30)
print(f'No. {"NOME":<10}  MÉDIA')
print('-'*30)
for i, a in enumerate(nomes):
    print(f'{i}  {nomes[i]:<12} {medias[i]}')
print('-'*30)
mostrar = 0
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'Notas de {nomes[mostrar]} são {notas[mostrar]}')
    print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

