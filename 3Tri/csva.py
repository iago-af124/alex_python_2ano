import csv

def cadastrar_jogador():
    nome = input('Nome: ')
    idade = input('Idade: ')
    pontuacao = input('Pontuacao: ')

    with open('jogadores.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome,idade,pontuacao])

    print('Jogador Salvo')

def ver_jogadores():
    with open('jogadores.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)

        print('=== JOGADORES ===')

        for linha in leitor:
            nome = linha[0]
            idade = linha[1]
            pontuacao = linha[2]

            print(f'{nome} - {idade} - {pontuacao}')

def ver_ranking():
    with open('jogadores.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)

        jogadores = []

        for linha in leitor:
            nome = linha[0]
            idade = linha[1]
            pontuacao = int(linha[2])

    jogadores.append(key=lambda x: x[2], reverse=True)

    print('=== RANKING ===')

    posicao = 1

    for jogador in jogadores:
        print(f'{posicao} - {jogador[0]} - {jogador[2]}')
        posicao += 1

def gerar_relatorio():
    with open('jogadores.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)

        jogadores = []

        for linha in leitor:
            nome = linha[0]
            idade = linha[1]
            pontuacao = int(linha[2])

            jogadores.append([nome, idade, pontuacao])
    total_pontos = 0
    maior_pontuacao = 0
    melhor_jogador = ''

    for jogador in jogadores:
        pontos = jogador[2]

        total_pontos += pontos

        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
            melhor_jogador = jogador[0]
    media = total_pontos /len(jogadores)

    print('=== Relatorio ===')
    print(f'Total de jogadores: {len(jogadores)}')
    print(f'Media de pontuação: {media:.2f}')
    print(f'Melhor jogador: {melhor_jogador}')
    print(f'Maior pontuação: {maior_pontuacao}')

while True:
    print('\n1. Cadastrar')
    print('2. Ver Jogadores')
    print('3. Ver Ranking')
    print('4. Ver Relatorio')
    print('5. Sair')

    opcao = input('Escolha uma opção:')

    if opcao == '1':
        cadastrar_jogador()
    elif opcao == '2':
        ver_jogadores()
    elif opcao == '3':
        ver_ranking()
    elif opcao == '4':
        gerar_relatorio()
    elif opcao == '5':
        print('Saindo...')
        break
    else:
        print('Opcao invalida')