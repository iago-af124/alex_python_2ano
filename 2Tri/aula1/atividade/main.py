from roger1 import quadrado,retangulo,triangulo,circulo

while True():
    print('1 Quadrado')
    print('2 Retangulo')
    print('3 Triangulo')
    print('4 Circulo')
    print('5 Sair')

    opcao = int('Escolha a opcao')

    if opcao == 5:
        print('Saindo')
        break
    elif opcao == 1:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(quadrado(n1,n2))
    elif opcao == 2:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(retangulo)
    elif opcao == 3:
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))
        print(triangulo)
    elif opcao == 4:
        n1 = int(input('Digite o raio'))
        print(circulo(n1))
    else:
        print('error')
