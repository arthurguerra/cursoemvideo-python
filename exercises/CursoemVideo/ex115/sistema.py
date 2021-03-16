from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova Pessoa',
                     'Sair do Sistema'])
    if resposta == 1:
        # Listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa no arquivo!
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO!!! Digite uma opção válida!\033[m')
    sleep(1)
