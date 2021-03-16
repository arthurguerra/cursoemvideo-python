'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print('Antes = ', valores)
dobra(valores)
print('Depois = ', valores)'''
def dobra(lista):
    valores2 = []
    for v in valores:
        valores2.append(v * 2)
    print(valores2)



valores = [7, 5, 2, 0, 4]
print(valores)
dobra(valores)
print(valores)


def soma(* valores):
    s = 0
    for v in valores:
        s += v
    print(f'Somando os valores {valores} temos {s}')


soma(2, 5)
soma(2, 9, 4)