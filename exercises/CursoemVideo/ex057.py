sexo = str(input('Informe seu sexo: [M/F] ').upper().strip()[0])
while sexo not in 'FM':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: ').strip().upper()[0])
print('Sexo {} registrado com sucesso!'.format(sexo))
