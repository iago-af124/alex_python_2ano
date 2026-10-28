personagens = [
    {
        "nome": "Arthas",
        "classe": "Guerreiro",
        "nivel": 10,
        "inventario": [("Espada", "Arma"), ("Escudo", "Defesa")]
    }
]

personagens.append({
    "nome": "Luna",
    "classe": "Maga",
    "nivel": 8,
    "inventario": [("Cajado", "Arma"), ("Poção", "Cura")]
})

for personagem in personagens:
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print("Inventário:")
    for item in personagem["inventario"]:
        print("-", item[0], "-", item[1])
