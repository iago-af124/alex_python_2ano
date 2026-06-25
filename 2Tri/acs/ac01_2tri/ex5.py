from validate_docbr import CPF

cpf = CPF()
conjunto = set()
validado = 0
n_validado = 0
i = 0
while(True):
    cpf_add = input('Coloque CPFs:')
    conjunto.add(cpf_add)
    if cpf.validate(cpf_add) == True:
        validado += 1
    else:
        n_validado += 1

    i += 1
    pergunta = input('Quer continuar(S/N)')
    if pergunta == 'S':
        continue
    else:
        break
print(f'Validados:{validado}')
if i > len(conjunto):
    print('Tem repetição')
else:
    print('Não tem repetição')