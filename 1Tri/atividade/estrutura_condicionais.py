def main():
    notas = []
    nota_media = 0
    frequencia_aulas = 0
    
    def frequencias():
        global frequencia_aulas
        aulas_dadas = int(input('Adicione as aulas dadas'))
        aulas_assistidas = int(input('Adicione as aulas assistidas'))
        frequencia_aulas = (aulas_assistidas / aulas_dadas) * 100
        print(frequencia_aulas)
    frequencias()
    def nota():
        global nota_media
        i = 0
        while(i < 2):
            add_notas = float(input('adicione as notas'))
            notas.append(add_notas)
            i += 1
        nota_media = (notas[0] + notas[1]) / 2
        print(nota_media)
    nota()

    if(frequencia_aulas < 75):
        print('reprovado')
    elif(frequencia_aulas >= 75):
        if(nota_media > 7):
            print('aprovado')
        elif(nota_media >= 5 and nota_media <= 7):
            print('esta de recuperação')
        elif(nota_media < 5):
            print('reprovado')
        else:
            print('error')
    else:
        print('error')
main()