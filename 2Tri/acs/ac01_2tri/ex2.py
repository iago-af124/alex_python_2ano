assentos = ({
    1: 'LIVRE',
    2: 'OCUPADO',
    3: 'LIVRE',
    4: 'OCUPADO',
    5: 'OCUPADO',
    6: 'LIVRE',
    7: 'LIVRE',
    8: 'OCUPADO',
    9: 'LIVRE',
    10: 'OCUPADO',
    11: 'LIVRE',
    12: 'LIVRE',
    13: 'OCUPADO',
    14: 'OCUPADO',
    15: 'LIVRE',
    16: 'OCUPADO',
    17: 'LIVRE',
    18: 'OCUPADO',
    19: 'LIVRE',
    20: 'OCUPADO'
})


print('Todos os assentos:')
for i in assentos:
    print(i)

assentos_livres = 0
assentos_ocupados = 0

for i in range(1,21):
    if assentos[i] == 'LIVRE':
        assentos_livres += 1
    elif assentos[i] == 'OCUPADO':
       assentos_ocupados += 1

print(f'Quantidade de assentos ocupados:{assentos_ocupados}')
print(f'Quantidade de assentos livres:{assentos_livres}')


while True:
    pergunta = input('Quer ver de algum assento especifico? (S/N)')
    if pergunta == 'S':
        while True:
            procurar = int(input('Qual voce quer ver:'))
            print('O assento está:',assentos[procurar])
            continuar = input('Quer continuar? (S/N)')
            if continuar == 'S':
                print('Ok')
            else:
                print('BLZ voltando...')
                break
    else:
        print('BLZ fechando...')
        break
        