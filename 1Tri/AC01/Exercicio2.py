nota = float(input('Adicione a nota de desempenho:'))
faltas = int(input('Adicione a quantidade de faltas por ano'))
tempo = float(input('Adicione o tempo que está na empresa em anos'))
salario = float(input('Adicione o salario atual'))

bonusSN = ''
percen = 0

if faltas > 20:
    print('usuario não pode receber bonus')
    bonusSN = 'n'
elif nota  >= 9:
    if tempo >= 5:
        percen = 20
        bonusSN = 's'
    else:
        bonusSN = 's'
        percen = 15
elif nota >= 7 and nota <= 8.9:
    if tempo >= 3:
        bonusSN = 's'
        percen = 10
    else:
        bonusSN = 's'
        percen = 5
elif nota < 7:
    bonusSN = 'n'
    percen = 0
else:
    bonusSN = 'error'
    print('error')

bonus = percen * (salario / 100)
salario = salario + bonus

print(f'Recebe bonus? (s/n) resposta:{bonusSN}')
print(f'Percentual aplicado de {percen}%')
print(f'O bonus será de {bonus}')
print(f'O novo salario será de {salario}')