try: # onde geralmente ocorre o erro
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário terminou o programa!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # quando não houver erro
    print(f'O resultado é {r:.2f}')
finally: # finaliza o 'try', dando erro ou não.
    print(' << Volte sempre! Muito Obrigado >>')

'''
except Exception as erro: # tratamento de erro
    print(f'O problema encontrado foi {erro.__class__}')
'''
