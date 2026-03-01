valor_veiculo = float(input('Adicione o Valor do Veiculo:'))
valor_entrada = float(input('Adicione o Valor a Entrada:'))
quantidade_parcelas = int(input('Adicione a quantidades de parcelas:'))

valor_financiado = valor_veiculo - valor_entrada
porcen = ((20*valor_veiculo)/100)
juros = 0

if valor_entrada < porcen:
    print('Financiamento negado')
else:
    if (quantidade_parcelas <= 24):
        juros = 1.2
    elif (quantidade_parcelas >= 25 and quantidade_parcelas <= 48):
        juros = 1.5
    elif (quantidade_parcelas > 48):
        juros = 2

    valor_total_juros = valor_financiado*(1+(juros/100*quantidade_parcelas))
    valor_parcela = valor_total_juros / quantidade_parcelas

    print(f'Esse foi o valor financiado {valor_financiado}')
    print(f'Esse foi o Percentual {juros}')
    print(f'Valor final {valor_total_juros}')
    print(f'Valor de parcela {valor_parcela}')
