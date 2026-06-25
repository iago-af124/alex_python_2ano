conjunto = set()
i = 0
while(True):
    pessoas = input('Coloque nome de pessoas:')
    conjunto.add(pessoas)
    i += 1
    pergunta = input('Quer continuar(S/N)')
    if pergunta == 'S':
        continue
    else:
        break

print(f'Pessoas que acessaram o sistema (sem repetição):{set(conjunto)}')
print(f'Em ordem alfabetica:{sorted(conjunto)}') #botei sorted pra ficar em ordem alfabetica mó preguiça


if i > len(conjunto):
    print('Tem repetição')
else:
    print('Não tem repetição')
