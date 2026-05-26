from dados import add_array,jogadores_array,partidas_array,pontos_array

def cadastrar_jogador():
    tfp = ''
    tf = True

    while tf:
        jogador = input('Adicione o Jogador: ')
        partidas = int(input('Adicione a quantidade de partidas: '))
        pontos = int(input('Adicione a quantidade de pontos/gols que teve: '))
        
        add_array(jogador, partidas, pontos)
        
        tfp = input('Voce quer adicionar mais um? (S/N) ')

        if tfp == 'S':
            print('OK')
            continue
        elif tfp == 'N':
            print('OK voltando pro menu...')
            tf = False
        else:
            print('Coloque apenas S/N')
            print('Voltando pro menu...')
            tf = False

def jogadores_cadastrados():
    print('Jogadores:')
    for jogador in jogadores_array:
        print(jogador)
    print('Retornando...')

def relatorio():
    desempenho = ''
    print(f'Nome|Partidas|Pontos|Média por partida|Desempenho')

    for i in range(len(jogadores_array)):
        media = pontos_array[i]/partidas_array[i]
        if media >= 2:
            desempenho = 'Excelente'
        elif media <= 1.9 and media >= 1:
            desempenho = 'Bom'
        elif media > 1:
            desempenho = 'Precisa melhorar'
        print(f'{jogadores_array[i]}|{partidas_array[i]}|{pontos_array[i]}|{media}|{desempenho}')
    print('Retornando...')

def pesquisar_jogadores():
    pesquisa = input('Coloque o nome:')
    i = 0

    if pesquisa in jogadores_array:
        print('Encontrado')
        for i in range(len(jogadores_array)):
            if pesquisa == jogadores_array[i]:
                print(f'Nome:{jogadores_array[i]}')
                print(f'Partidas:{partidas_array[i]}')
                print(f'Gols/Pontos:{pontos_array[i]}')
    else:
        print('Não foi encontrado')

def alterar():
    print('Altere:')
    print('1 - Nome')
    print('2 - Partidas')
    print('3 - Gols/Pontos')
    opcao = int(input('Escolha:'))
    while True:
        if opcao == 1:
            sistema = input('De quem quer alterar(NOME):')
            for i in range(len(jogadores_array)):
                if sistema == jogadores_array[i]:
                    jogadores_array.remove(sistema)
                    sistema1 = input('Novo nome:')
                    jogadores_array.insert(i,sistema1)
                    print('Adicionado')
                    break
                else:
                    print('Ninguem foi encontrado')
            break
        elif opcao == 2:
            sistema = input('De quem quer alterar(NOME):')
            for i in range(len(jogadores_array)):
                if sistema == jogadores_array[i]:
                    partidas_array.remove(partidas_array[i])
                    sistema1 = int(input('Novas partidas:'))
                    partidas_array.insert(i, sistema1)
                    print('Alterado')
                    break
            else:
                print('Ninguem foi encontrado')
            break

        elif opcao == 3:
            sistema = input('De quem quer alterar(NOME):')
            for i in range(len(jogadores_array)):
                if sistema == jogadores_array[i]:
                    pontos_array.remove(pontos_array[i])
                    sistema1 = int(input('Novos gols/pontos:'))
                    pontos_array.insert(i, sistema1)
                    print('Alterado')
                    break
            else:
                print('Ninguem foi encontrado')
            break

def remover():
    pesquisa = input('Quem quer deletar do cadastro (NOME): ')
    if pesquisa in jogadores_array:
        print('Encontrado')
        for i in range(len(jogadores_array)):
            if pesquisa == jogadores_array[i]:
                jogadores_array.remove(pesquisa)
                pontos_array.pop(i)
                partidas_array.pop(i)
                print('Removido com sucesso')
                break
    else:
        print('Nao foi encontrado')

def estatisicas():
    maior_media = 0
    menor_media = 0
    soma_medias = 0
    melhor_jogador = ''
    excelente = 0
    precisa_melhorar = 0

    for i in range(len(jogadores_array)):
        media = pontos_array[i] / partidas_array[i]
        soma_medias += media

        if media > maior_media:
            maior_media = media
            melhor_jogador = jogadores_array[i]

        if i == 0:
            menor_media = media

        if media < menor_media:
            menor_media = media

        if media >= 2:
            excelente += 1
        elif media < 1:
            precisa_melhorar += 1

    media_geral = soma_medias / len(jogadores_array)

    print(f'Quantidade total de jogadores cadastrados: {len(jogadores_array)}')
    print(f'Maior media de desempenho: {maior_media}')
    print(f'Menor media de desempenho: {menor_media}')
    print(f'Media geral dos jogadores: {media_geral}')
    print(f'Jogador com melhor desempenho: {melhor_jogador}')
    print(f'Jogadores com desempenho excelente: {excelente}')
    print(f'Jogadores que precisam melhorar: {precisa_melhorar}')
    print('Retornando...')