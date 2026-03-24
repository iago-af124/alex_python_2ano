import random

#1. Criação do Personagem
def criacao_personagem():
    personagem = input("Coloque o nome de seu personagem: ")
    classe = input("Coloque a classe do personagem (Guerreiro, mago ou arqueiro): ")
    forca = int(input("Coloque a força do seu personagem: "))
    magia = int(input("Coloque o valor da magia: "))
    agilidade = int(input("Coloque o valor da agilidade: "))
    return personagem, classe, forca, magia, agilidade

#2. Cálculo do Poder do Personagem
def poder_personagem(f, m, a):
    return (f * 2) + m + a

#3. Classificação do Personagem (Ranking)
def classificacao(poder):
    if poder < 100:
        return 'Bronze'
    elif poder >= 100 and poder <= 199:
        return 'Prata'
    elif poder >= 200 and poder <= 499:
        return 'Ouro'
    else:
        return 'Lendario'

#inimigo
def inimigo():
    inimigo_vida = random.randint(7, 20)
    inimigo_defesa = random.randint(1, 10)
    inimigo_ataque = random.randint(2, 6)
    inimigo_dano = max(0, inimigo_ataque - inimigo_defesa)
    return inimigo_vida, inimigo_defesa, inimigo_ataque, inimigo_dano

#Relatorio final
def relatorio_final(personagem, classe, poder, calc_inimigos):
    print("RELÁTORIO FINAL DO JOGADOR!")
    print(f"Nome do personagem: {personagem}")
    print(f"Classe escolhida: {classe}")
    print(f"Poder total: {poder}")
    print(f"Classificação no ranking: {classificacao(poder)}")
    print(f"Total de inimigos derrotados: {calc_inimigos}")

#sistema de batalha
def batalha_sistema(personagem, classe, poder):
    vida_personagem = 30
    calc_inimigos = 0

    while vida_personagem > 0:
        inimigo_vida, inimigo_defesa, inimigo_ataque, inimigo_dano = inimigo()
        critico_usado = False

        print(f'Novo inimigo! (Vida: {inimigo_vida} | Ataque: {inimigo_ataque} | Defesa: {inimigo_defesa})')

        while vida_personagem > 0 and inimigo_vida > 0:
            print('/')
            print(f'vida do inimigo: {inimigo_vida}')
            print(f'vida do personagem: {vida_personagem}')
            print('/')

            ataque = input('Aperte enter para atacar: ')
            if ataque == '':
                if not critico_usado:
                    critico = input('O ataque foi critico? (s/n): ')
                    if critico == 's':
                        print('Ataque CRITICO com sucesso (-2 de vida do inimigo)')
                        inimigo_vida -= 2
                        critico_usado = True
                    else:
                        print('Ataque com sucesso (-1 de vida do inimigo)')
                        inimigo_vida -= 1
                else:
                    print('Ataque com sucesso (-1 de vida do inimigo)')
                    inimigo_vida -= 1
            else:
                print('Aperte Enter e não outro digito')
                continue

            if inimigo_vida <= 0:
                print('Inimigo derrotado!')
                calc_inimigos += 1
                break

            print('O inimigo vai atacar')
            ataque_ini = random.randint(1, 5)
            if ataque_ini <= 3:
                if inimigo_dano == 0:
                    print('Nao deu nenhum dano')
                else:
                    print(f'Voce nao conseguiu esquivar (-{inimigo_dano} de vida)')
                    vida_personagem -= inimigo_dano
            else:
                print('Voce conseguiu esquivar (nenhuma mudança na sua vida)')

        if vida_personagem <= 0:
            print('Voce foi derrotado!')
            relatorio_final(personagem, classe, poder, calc_inimigos)
            break

        continuar = input('Deseja continuar? (s/n): ')
        if continuar != 's':
            print('Voce encerrou a aventura.')
            relatorio_final(personagem, classe, poder, calc_inimigos)
            break

    return calc_inimigos, vida_personagem

personagem, classe, forca, magia, agilidade = criacao_personagem()
poder = poder_personagem(forca, magia, agilidade)
print(f'Poder total: {poder}')
print(f'Classificação: {classificacao(poder)}')
calc_inimigos, vida_personagem = batalha_sistema(personagem, classe, poder)