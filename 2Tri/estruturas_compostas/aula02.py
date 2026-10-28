produtos = [
    {"nome": "Camiseta", "preco": 49.90, "quantidade": 10},
    {"nome": "Calça", "preco": 89.90, "quantidade": 5},
    {"nome": "Tênis", "preco": 159.90, "quantidade": 3}
]

for produto in produtos:
    print("Nome:", produto["nome"])
    print("Preço: R$", produto["preco"])
    print("Quantidade:", produto["quantidade"])
