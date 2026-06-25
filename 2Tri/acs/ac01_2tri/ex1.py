meses = ([
    "Janeiro", 
    "Fevereiro", 
    "Março", 
    "Abril", 
    "Maio", 
    "Junho", 
    "Julho", 
    "Agosto", 
    "Setembro", 
    "Outubro", 
    "Novembro", 
    "Dezembro"
])

vendas = ({
    1: [1,223,32],
    2: [12,123],
    3: [938,1],
    4: [213,23792797124624124],
    5: [213,23792797124624124],
    6: [12,1],
    7: [1239,23,32],
    8: [12,1,1,1,1,1],
    9: [2313,33],
    10: [12323,121,12,43],
    11: [1298,209,213,2],
    12: [1223456,3]
})

somador = []

#Kaique online
print('Mostrar o maior valor de venda')
for i in range(1,12):
    array = vendas[i]
    array_soma = sum(array)
    somador.append(array_soma)

media = sum(somador) / len(somador)

print(f'O maior valor de venda: {max(somador)}')
print(f'O menor valor de venda: {min(somador)}')

for i in range(len(somador)):
    if somador[i] > media:
        print(f'Mês que aconteceu a maior venda acima da media:{meses[i]}')

print(f'Média anual de vendas:{media}')
#Kaique Mode Active tuntun
meses_array = []

for i in range(1,12):
    array2 = vendas[i]
    array_soma2 = sum(array2)
    meses_array.append(array_soma2)
maior_meses = meses_array.index(max(meses_array))
menor_meses = meses_array.index(min(meses_array))

print(f'Mes com maior venda:{meses[maior_meses]}')
print(f'Mes com menor venda:{meses[menor_meses]}')
#Kaique emoji easter egg 🙂