def leiaDinheiro(msg):
    válido = False
    while not válido:
        n = str(input(msg).replace(',', '.'))
        try:
            float(n)
            válido = True
        except ValueError:
            print(f'\033[1;31mERRO: "{n}" é um preço inválido!\033[m')
    return float(n)


'''def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg).replace(',', '.')).strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! "{entrada}" é um preço inválido!')
        else:
            válido = True
    return float(entrada)'''''
