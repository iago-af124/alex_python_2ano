veiculos = []

while(True):
    marca = input('marca: ')
    modelo = input('modelo: ')
    ano = int(input('ano: '))
    cor = input('cor: ')
    valor = float(input('valor: '))

    if (2026 - ano) >= 20:
        status = 'Antigo'
    else:
        status = 'Moderno'

    if valor > 100000:
        desconto = valor * 0.10
    else:
        desconto = 0

    valor_final = valor - desconto

    veiculos.append([marca, modelo, ano, cor, status, valor, desconto, valor_final])

    pergunta = input('Quer continuar(S/N)')
    if pergunta == 'S':
        continue
    else:
        break

for i in range(len(veiculos)):
    carro = veiculos[i]
    print(f'Marca: {carro[0]}')
    print(f'Modelo: {carro[1]}')
    print(f'Ano: {carro[2]}')
    print(f'Cor: {carro[3]}')
    print(f'Classificação: {carro[4]}')
    print(f'Valor Original: R${carro[5]}')
    
    if carro[6] > 0:
        print(f'Desconto Aplicado (10%): R${carro[6]}')
        
    print(f'Valor Final: R${carro[7]}')