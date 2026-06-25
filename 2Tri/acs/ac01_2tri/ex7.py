estoque = {}

estoque['nome'] = input('Nome do produto: ')
estoque['preco'] = float(input('Preço: '))
estoque['quantidade'] = int(input('Quantidade: '))

while(True):
    print('1. Exibir produto')
    print('2. Alterar preço')
    print('3. Alterar quantidade')
    print('4. Calcular valor total em estoque')
    print('5. Encerrar sistema')
    
    opcao = input('Escolha a opção (1 a 5): ')

    if opcao == '1':
        print(f"Produto: {estoque['nome']}")
        print(f"Preço: R${estoque['preco']}")
        print(f"Qtd: {estoque['quantidade']}")
    elif opcao == '2':
        estoque['preco'] = float(input('Novo preço: '))
        print('Preço atualizado!')
    elif opcao == '3':
        estoque['quantidade'] = int(input('Nova quantidade: '))
        print('Quantidade atualizada!')
    elif opcao == '4':
        total = estoque['preco'] * estoque['quantidade']
        print(f'Valor total no estoque: R${total}')
    elif opcao == '5':
        print('fechando...')
        break
    else:
        print('Coloque uma dessa opções')
        continue