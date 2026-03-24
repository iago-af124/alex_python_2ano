import random

#1. Criação do Personagem
def criacao_personagem():
    personagem = (input("Coloque o nome de seu personagem: "))
    classe = (input("Coloque a classe do personagem (Guerreiro, mago ou arqueiro.): "))
    forca = int(input("Coloque a força do seu personagem: "))
    magia = int(input("Coloque o valor da magia: "))
    agilidade = (input("Coloque o valor da agilidade: "))
    return personagem,classe,magia,forca,agilidade

#2. Cálculo do Poder do Personagem
def poder_personagem(f,m,a):
    return (f*2) + m + a

#3. Classificação do Personagem (Ranking)
def classificacao(poder):
    if poder < 100:
        print('Classificação: Bronze')
    elif poder >= 100 and poder <= 199:
        print('Classificação: Prata')
    elif poder >= 200 and poder <= 499:
        print('Classificação: Ouro')
    elif poder > 500:
        print('Classificação: Lendario')
    else:
        print('error')

def inimigo():
    inimigo_vida = random.randint(7,20)
    inimigo_defesa = random.randint(1,10)
    inimigo_ataque = random.randint(1,10)
    inimigo_dano = inimigo_ataque - inimigo_defesa
    return inimigo_vida,inimigo_defesa,inimigo_ataque,inimigo_dano

inimigo_vida,inimigo_defesa,inimigo_ataque,inimigo_dano = inimigo()

def batalha_sistema():
    batalha = True

    vida_personagem = 10
    ataque_critico = random.randint(1,2)
    ataque_ini = random.randint(1,5)

    def status_batalha():
        print('/')
        print(f'vida do inimigo:{inimigo_vida}')
        print(f'vida do personagem:{vida_personagem}')
        print('/')

    while(batalha):
        status_batalha()

        if inimigo_vida <= 0:
            batalha = False
            break

        #hora que o usuario vai atacar
        ataque = input('Aperte enter para atacar')
        if ataque == '':
            if ataque_critico == 1:
                print('Ataque CRITICO com sucesso (-2 de vida do inimigo)')
                inimigo_vida -= 2
            elif ataque_critico == 2:
                print('Ataque com sucesso (-1 de vida do inimigo)')
                inimigo_vida -= 1
            else:
                print('error')
        else:
            print('Aperte Enter e não outro digito')

        #hora que o inimigo vai atacar
        print('O inimigo vai atacar')
        if ataque_ini <= 3:
            print(f'Voce não conseguiu esquivar (-{inimigo_dano} de vida)')
            vida_personagem -= inimigo_dano
        elif ataque_ini > 5:
            print('Voce conseguiu esquivar (nenhuma mudança na sua vida)')
    

personagem,classe,magia,forca,agilidade = criacao_personagem()
poder = poder_personagem(forca,magia,agilidade)

#Batalha
def main():
    rodar = True

    while(rodar):
        criacao_personagem()
        print(f'A quantidade do poder de seu personagem {poder}')

        print('A um inimigo na sua frente')

main()
