p = float(input('Digite o preço do produto: '))
d = int(input('Digite a porcentagem do desconto: '))
p2 = (p/100)*d
print('O valor do produto com {}% de desconto terá um abatimento de {} reais e sairá por {}'.format(d, p2, p-p2))