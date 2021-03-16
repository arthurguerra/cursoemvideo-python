nome = str(input('Qual é o seu nome? ')).strip()
if nome.lower() == 'arthur':
    print('Que nome bonito!')
elif nome.lower() == 'pedro' or nome == 'joão' or nome == 'maria':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Claudia Jéssica Jessica Marina Mariana':
    print('Belo nome feminino')
elif nome.lower() == 'beatriz':
    print('Você é o amor da minha vida!')

print('Tenha um bom dia, {}!'.format(nome))