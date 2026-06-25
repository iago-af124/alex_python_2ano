conjunto = set()


while True:
    hashtag = input('Adicione a hashtag: #') 
    conjunto.add(hashtag)
    continuar = input('Adicionar mais? (S/N)')

    if continuar == 'S':
        continue
    else:
        break

print(f'Quantidade total de hashtags únicas:{len(conjunto)}')
print(f'Lista das hashtags:{conjunto}')
while True:
    identificador = input('Quer encontrar determinadas hashtags se existem no conjunto')
    if identificador == 'S':
        identificador2 = input('Escreva pra identificar:')
        if identificador2 in conjunto:
            print('Ele ta lá')
            break
        else:
            print('Não ta la')
            break
    else:
        break