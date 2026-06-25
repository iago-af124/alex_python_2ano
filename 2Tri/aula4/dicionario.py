aluno = {
    'nome':'Teclado',
    'idade': 15
}
print('===VISUALIZANDO UM VALOR===')
print(aluno['nome'])

print('===ALTERANDO VALOR===')
aluno['idade']=16
print(aluno['idade'])

print('===ADICIONANDO UMA PROPRIEDADE===')
aluno['cidade'] = 'São Paulo'
print(aluno)

print('===REMOVENDO UMA PROPRIEDADE===')
del aluno['idade']
print(aluno)

print('===PERCORRENDO UM DICIONARIO===')
for chave,valor in aluno.items():
    print(chave,':',valor)