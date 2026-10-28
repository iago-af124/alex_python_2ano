from cadastro import adicionar
from relatorio import relatorio
from buscar import buscar_equipamento
from historico import historico

while True:
    print('1 - Cadastrar equipamento')
    print('2 - Ver histórico')
    print('3 - Listar inventário completo e gerar relatório')
    print('4 - Buscar equipamento detalhado')
    print('5 - Sair')

    opcao = input('Escolha uma das opções: ').strip()

    if opcao == '1':
        adicionar()
    elif opcao == '2':
        historico()
    elif opcao == '3':
        relatorio()
    elif opcao == '4':
        buscar_equipamento()
    elif opcao == '5':
        print('Saindo')
        break
    else:
        print('Opção inválida')