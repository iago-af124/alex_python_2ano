def verRanking():
    arquivo = open('jogadores.txt', 'r')
    linhas = arquivo.readline()
    arquivo.close()

    print('Jogador Salvo')

    for linha in linhas:
        print(linha)

def cadastrarJogador():
    nome = input('Digite seu nome:')
    pontuacao = input('Digite sua pontuação:')

    arquivo = open('jogador.txt','a')
    arquivo.write(nome + '-' + pontuacao + '\n')
    arquivo.close()

    print('Jogador salvo!')

while True:
    print('1 - Cadastrar jogador')
    print('2 - Ver ranking')
    print('3 - Sair')

    opcao = input('Escolha uma opcao:')

    if opcao == '1':
        cadastrarJogador()
    elif opcao == '2':
        verRanking()
    elif opcao == '3':
        print('Saindo do sistema...')
        break
    else:
        print('Opcao invalida')
