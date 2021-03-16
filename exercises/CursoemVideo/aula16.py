lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos + 1}')

print('Comi pra caramba!')

