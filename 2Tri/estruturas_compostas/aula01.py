catalogo_filmes = [
    ["Ação", "Velozes e Furiosos", "Homem-Aranha", "Batman"],
    ["Comédia", "As Branquelas", "Gente Grande", "Todo Mundo em Pânico"],
    ["Animação", "Toy Story", "Shrek", "Procurando Nemo"]
]

for categoria in catalogo_filmes:
    print("Categoria:", categoria[0])
    for filme in categoria[1:]:
        print("-", filme)
