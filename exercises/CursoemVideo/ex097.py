def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'  {texto}')
    print('~' * tam)


escreva(str(input('Digite um texto: ')))