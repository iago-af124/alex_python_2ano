from roger import soma,subtrair,multiplicacao,dividir

while True:
    print('Escolha a opção hahaha roger')
    print('1 Somar')
    print('2 Subtrair')
    print('3 Multiplicar')
    print('4 Divir')
    print('5 Sair')

    opcao = int(input('Escolha oq vc quer hahahah roger'))

    if opcao == 5:
        print('tchau goma')
        break
    elif opcao == 1:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(soma(n1,n2))
    elif opcao == 2:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(subtrair(n1,n2))
    elif opcao == 3:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(multiplicacao(n1,n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(dividir(n1,n2))
    else:
        print('opcao invalida')
