cidade = str(input('Em que cidade você nasceu? ')).strip()
print('santo' in cidade.lower().split()[0])
print(cidade[:5].upper() == 'SANTO')
