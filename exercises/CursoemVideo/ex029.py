v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite de 80km/h')
    print('Você deve pagar uma multa de: R${:.2f}'.format((v-80)*7))
print('Tenha um bom dia! Diriga com segurança!')