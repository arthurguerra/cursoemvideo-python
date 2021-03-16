def notas(*n, sit=False):
    """
    -> Função para analisar a nota e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: (opcional) indicador para mostrar ou não a situação da turma.
    :return: dicionário com  informações sobre a turma.
    """
    turma = {}
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / len(n)
    if sit:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] < 5:
            turma['situação'] = 'RUIM'
        else:
            turma['situação'] = 'RAZOÁVEL'
    print('-' * 40)
    return turma


# PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
