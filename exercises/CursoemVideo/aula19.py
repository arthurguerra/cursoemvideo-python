estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v} ', end='')
    print()

ranking = sorted(alunos, key=lambda k: k['número'])
