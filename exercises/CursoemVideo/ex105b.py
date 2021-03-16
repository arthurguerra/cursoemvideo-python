def notas(lst, sit=False):
    """
    -> Função para analisar notas de vários alunos e sua respectiva situação.
    :param lst: lista com uma ou mais notas da turma
    :param sit: (opcional), indicador se deve ou não adicionar a situação ao dicionário.
    :return: dicionário com a análisa da situação da turma.
    """
    dicio = {'total': len(lst), 'maior': max(lst), 'menor': min(lst),
             'média':sum(lst) / len(lst)}
    if sit:
        if dicio['média'] < 5:
            s = 'RUIM'
        elif 5 < dicio['média'] < 7:
            s = 'RAZOÁVEL'
        else:
            s = 'BOA'
        dicio['situação'] = s
    return dicio


nota = []
quant = int(input('Quantas notas você quer analisar? '))
for c in range(quant):
    nota.append(float(input(f'{c+1}ª Nota: ')))
print(notas(nota, sit=True))
