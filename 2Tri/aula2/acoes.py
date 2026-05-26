from sistema import delivery

def opcao():
    while True:
        print('1. Peça o Pedido\n2. Saia')
        opcao = int(input('Escolha qual deseja:'))

        if opcao == 1:
            print("1 - Pedido entregue rapidamente")
            print("2 - Pedido entregue corretamente")
            print("3 - Comida chegou quente")
            print("4 - Atendimento educado ao cliente")
            print("5 - Cliente deu avaliação 5 estrelas")
            print("6 - Embalagem bem organizada")
            print("7 - Pedido chegou antes do prazo")
            print("8 - Resolver problema do cliente com eficiência")
            print("9 - Boa comunicação com o cliente")
            print("10 - Entregador simpático")
            print("11 - Pedido completo sem faltar itens")
            print("12 - Cliente ficou satisfeito com o serviço")
            print("13 - Entrega em condições difíceis")
            print("14 - Restaurante preparou pedido rapidamente")
            print("15 - Pedido bem protegido")
            print("16 - Pedido atrasado")
            print("17 - Pedido entregue errado")
            print("18 - Comida chegou fria")
            print("19 - Cliente insatisfeito")
            print("20 - Pedido incompleto")
            print("21 - Entregador mal educado")
            print("22 - Erro no endereço de entrega")
            print("23 - Cancelamento de pedido")
            print("24 - Demora excessiva no preparo")
            print("25 - Falta de comunicação com o cliente")
            print("26 - Cobrança incorreta")
            print("27 - Problema na embalagem")
            print("28 - Produto derramado ou danificado")
            print("29 - Cliente deu avaliação baixa")
            print("30 - Pedido não foi entregue")
        elif opcao == 2:
            print('Obrigado por usar bye bye')
            break
        else:
            print('Coloque algo que esta na lista')
            return