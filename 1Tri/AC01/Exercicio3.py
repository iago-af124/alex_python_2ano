renda = float(input('Adicione a renda mensal'))
divida = float(input('Adicione o valor da sua divida atual'))
score = int(input('Adicione o score de credito:'))

compromentimento = (divida / renda) * 100

credito = ''
taxa = 0

if compromentimento > 50:
    credito = 'negado'
elif score >= 800:
    if compromentimento <= 30:
            credito = 'aprovado'
            taxa = 1
    else:
        credito = 'aprovado'
        taxa = 1.5
elif score >= 600 and score <= 799:
    if compromentimento <= 30:
        credito = 'aprovado'
        taxa = 2
    else:
        credito = 'aprovado'
        taxa = 2.5
elif score < 600:
    credito = 'aprovado'
    taxa = 3.5
else:
    print('error')

print(f'Percentual de comprometimento:{compromentimento}%')
print(f'Credito:{credito}')
print(f'Taxa:{taxa}')

            