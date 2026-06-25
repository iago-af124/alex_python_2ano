nomes = {'Ana','Carlos','Ana'}

print('===Exibindo o Conjunto===')
print(nomes)

nomes.add('Ronaldo')
print('===Exibindo o conjunto apos inclusao===')
print(nomes)

nomes.remove('Carlos')
print('===Exibindo o conjunto apos remover===')
print(nomes)

print('===Percorrendo o conjunto===')
for nome in nomes:
    print(nome)