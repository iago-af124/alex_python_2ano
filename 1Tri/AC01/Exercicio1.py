veiculo = float(input('Adicione o Valor do Veiculo:'))
entrada = float(input('Adicione o Valor a Entrada:'))
parcelas = int(input('Adicione a quantidades de parcelas:'))

valor_financiado = veiculo - entrada
percen = ((20*veiculo)/100)
juros = 0

if entrada < percen:
    print('Financiamento negado')
else:
    if (parcelas <= 24):
        juros = 1.2
    elif (parcelas >= 25 and parcelas <= 48):
        juros = 1.5
    elif (parcelas > 48):
        juros = 2

    valor_total_juros = valor_financiado*(1+(juros/100*parcelas))
    valor_parcela = valor_total_juros / parcelas

    print(f'Esse foi o valor financiado {valor_financiado}')
    print(f'Esse foi o Percentual {juros}')
    print(f'Valor final {valor_total_juros}')
    print(f'Valor de parcela {valor_parcela}')
