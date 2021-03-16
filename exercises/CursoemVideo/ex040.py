n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
cores = {'limpa': '\033[m', 'vermelho':'\033[31m', 'verde': '\033[32m', 'amarelo':'\033[33m'}
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, média))
if média < 5.0:
    print('O aluno está {}REPROVADO{}!'.format(cores['vermelho'], cores['limpa']))
elif 5.0 < média < 7.0:
    print('O aluno está em {}RECUPERAÇÃO{}!'.format(cores['amarelo'], cores['limpa']))
else:
    print('O aluno está {}APROVADO{}!'.format(cores['verde'], cores['limpa']))