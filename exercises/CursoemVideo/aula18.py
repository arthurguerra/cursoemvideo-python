galera = list()
dado = []
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade e tem {p[1]} anos')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade. ({p[1]} anos)')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
'''dados = []
for c in range(0, 3):
    pessoa = []
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Idade: ')))
    dados.append(pessoa[:])
for c in range(0, len(dados)):
    for p in range(0, len(dados[c])):
        print(dados[c][p], end=' ')
    print()
print(dados)'''
