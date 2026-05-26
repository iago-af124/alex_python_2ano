from funcoes import cadastrar_jogador,jogadores_cadastrados,relatorio,pesquisar_jogadores,alterar,remover,estatisicas

def menu():
    selec = [
        '1. Cadastrar novo jogador',
        '2. Mostrar todos os jogadores cadastrados',
        '3. Mostrar relatório completo',
        '4. Pesquisar jogador pelo nome',
        '5. Alterar informações de um jogador',
        '6. Remover jogador do cadastro',
        '7. Mostrar estatísticas gerais',
        '8. Encerrar programa'
    ]

    while(True):
        for i in range(8):
            print(selec[i])

        opcao = int(input('Escolha a sua opção:'))
        if opcao == 1:
            cadastrar_jogador()
        elif opcao == 2:
            jogadores_cadastrados()
        elif opcao == 3:
            relatorio()
        elif opcao == 4:
            pesquisar_jogadores()
        elif opcao == 5:
            alterar()
        elif opcao == 6:
            remover()
        elif opcao == 7:
            estatisicas()
        elif opcao == 8:
            print('Encerrando...')
            break
        else:
            print('Coloque um numero')
            return 
menu()