def primeiro():
    alex = float(input('Adicione um número bem legal:'))

    if alex > 0:
        print('é positivo')
    elif alex < 0:
        print('lenovo')
    else:
        print('coloque um numero imbecil')

def segundo():
    roger = float(input('digite sua idade:'))

    if roger >= 18:
        print('maior de idade')
        
    else:
        print('menor de idade') 

def terceiro():
    iago = float(input('digite sua idade:'))

    if iago >= 16:
        print('pode votar')
        
    else:
        print('não pode') 

def quarto():
    max = float(input('digite sua nota:'))

    if max >= 6:
        print('aprovado')
    elif max >= 4 and max <= 5.9:
        print('recuperação')
    else:
        print('reprovado')

def main():
    primeiro()
    segundo()
    terceiro()
    quarto()
    print('acabou seu bobao')
print(main())
