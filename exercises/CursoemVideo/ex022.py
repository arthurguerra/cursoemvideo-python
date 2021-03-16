nome = str(input('Digite seu nome: '))
print('Maiúscula: {}.'.format(nome.upper()))
print('Minúscula: {}.'.format(nome.lower()))
print('Total de letras: {}.'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('O seu primeiro nome é {} e possui {} letras.'.format(dividido[0], len(dividido[0])))




