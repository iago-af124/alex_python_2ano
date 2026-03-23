#1. Criação do Personagem
def criacao_personagem(personagem,classe,forca,magia,agilidade):
    personagem = (input("Coloque o nome de seu personagem: "))
    classe = (input("Coloque a classe do personagem (Guerreiro, mago ou arqueiro.): "))
    forca = int(input("Coloque a força do seu personagem: "))
    magia = int(input("Coloque o valor da magia: "))
    agilidade = (input("coloque o valor da agilidade: "))
    return personagem,classe,magia,forca,agilidade

#2. Cálculo do Poder do Personagem
def poder_personagem(f,m,a):
    return f*2 + m + a

#3. Classificação do Personagem (Ranking)
def classificacao():
    if poder_personagem() < 100:
        print('Classificação: Bronze')
    elif poder_personagem() >= 100 and poder_personagem() <= 199:
        print('Classificação: Prata')
    elif poder_personagem() >= 200 and poder_personagem() <= 499:
        print('Classificação: Ouro')
    elif poder_personagem() > 500:
        print('Classificação: Lendario')
    else:
        print('error')

#Batalha
def main():
    
    while(True):
        print('fiejao')