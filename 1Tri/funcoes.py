def soma(a,b):
    a = float(input('Digite o primeiro numero:'))
    b = float(input('Digirte o segundo numero:')) 
    return a + b

def subtracao(a,b):
    resultado = a - b
    print('Resultado:', resultado)

def multiplicacao():
    a = float(input('Digite o primeiro numero:'))
    b = float(input('Digirte o segundo numero:')) 
    return a * b

def divisao(a,b):
    return a / b

print('Escolha a operação:')
print('1 - soma')
print('2 - subtração')
print('3 - multiplicacao')
print('4 - divisao')

opcao = int(input('Opção:'))

if opcao == 1:
    soma()
elif opcao == 2:
    n1 = float(input('Digite o primeiro numero:'))
    n2 = float(input('Digirte o segundo numero:')) 
    subtracao(n1,n2)
elif opcao == 3:
    resultado = multiplicacao()
    print('Resultado:', resultado)
elif opcao == 4:
    n1 = float(input('Digite o primeiro numero:'))
    n2 = float(input('Digirte o segundo numero:')) 
    resultado = divisao(n1,n2)
    print('ResultadO:',resultado)
else:
    print('Opção invalida')
