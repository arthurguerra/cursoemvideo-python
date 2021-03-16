pilha = list()
exp = str(input('Digite a expressão: '))
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        elif len(pilha) == 0:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está errada! ')
#if exp.count('(') == exp.count(')'):
#    print('Sua expressão está válida!')
#else:
#    print('Sua expressão está errada!')