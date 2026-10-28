palestrantes = [
    {"nome": "Alan Turing", "tema": "Futuro da IA", "horario": "10:00"},
    {"nome": "Ada Lovelace", "tema": "Algoritmos", "horario": "14:00"},
    {"nome": "Grace Hopper", "tema": "Compiladores", "horario": "16:00"}
]

empresas_participantes = [
    {
        "empresa": "DevMakers",
        "pavilhao": "Pavilhao Dev",
        "estande_numero": 12,
        "brindes_disponiveis": [
            ("Caneca", "Premium"),
            ("Adesivo", "Comum")
        ]
    },
    {
        "empresa": "CyberAI",
        "pavilhao": "Pavilhao AI",
        "estande_numero": 5,
        "brindes_disponiveis": [
            ("Mousepad", "Premium"),
            ("Caneta", "Comum")
        ]
    }
]

def cadastrar_palestrante():
    print("Novo Cadastro")
    nome = input("Nome: ")
    tema = input("Tema: ")
    horario = input("Horario: ")
    novo = {
        "nome": nome,
        "tema": tema,
        "horario": horario
    }
    palestrantes.append(novo)
    print("Cadastro com sucesso!")

opcao = -1

while opcao != 0:
    print("1 - Mapa dos Pavilhoes")
    print("2 - Mostrar Palestrantes")
    print("3 - Cadastrar Palestrante")
    print("4 - Ficha do Estande")
    print("5 - Catalogo de Brindes")
    print("6 - Relatorio Integrador")
    print("0 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        pavilhoes_estandes = [
            ["Pavilhao AI", "Microsoft", "Google", "AWS"],
            ["Pavilhao Dev", "GitHub", "StackOverflow", "JetBrains"],
            ["Pavilhao Hardware", "NVIDIA", "Intel", "AMD"]
        ]
        print("Mapa dos Pavilhoes:")
        for pavilhao in pavilhoes_estandes:
            print(pavilhao[0] + ":")
            for estande in pavilhao[1:]:
                 print("-", estande)

    elif opcao == 2:
        print("Cronograma:")
        for p in palestrantes:
            print("Nome:", p["nome"])
            print("Tema:", p["tema"])
            print("Horario:", p["horario"])
            print("---")

    elif opcao == 3:
        cadastrar_palestrante()

    elif opcao == 4:
        estande = {
            "nome_empresa": "TechCorp",
            "numero_estande": 42,
            "brindes": []
        }
        estande["brindes"].append("Adesivo")
        estande["brindes"].append("Camiseta")
        estande["brindes"].append("Chaveiro")
        print("Ficha do Estande")
        print("Empresa:", estande["nome_empresa"])
        print("Numero:", estande["numero_estande"])
        print("Brindes:")
        for b in estande["brindes"]:
            print("-", b)

    elif opcao == 5:
        catalogo_brindes = [
            ("Squeeze", "Utensilio"),
            ("Caderno", "Papelaria"),
            ("Mochila", "Acessorio"),
            ("Caneta", "Papelaria")
        ]
        print("Catalogo Fixo:")
        for brinde in catalogo_brindes:
            print("Brinde:", brinde[0], "| Categoria:", brinde[1])

    elif opcao == 6:
        print("Relatorio Completo:")
        for e in empresas_participantes:
            print("Empresa:", e["empresa"])
            print("Pavilhao:", e["pavilhao"])
            print("Estande:", e["estande_numero"])
            print("Brindes:")
            for b in e["brindes_disponiveis"]:
                print("-", b[0], "(", b[1], ")")
            print("---")
#kaique easter egg yy
    elif opcao == 0:
        print("Saindo do sistema...")

    else:
        print("Opcao invalida!")
