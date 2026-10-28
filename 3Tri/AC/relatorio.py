import csv

def relatorio():
    try:
        with open('equipamentos.csv', 'r', encoding='utf-8') as arquivocsv:
            leitor = csv.reader(arquivocsv)
            equipamentos = []

            print("\n inventario ")
            for linha in leitor:
                if len(linha) == 3:
                    nome = linha[0]
                    patrimonio = linha[1]
                    valor = float(linha[2])
                    equipamentos.append((nome, patrimonio, valor))
                    print(f"Nome: {nome} | Patrimônio: {patrimonio} | Valor: R$ {valor:.2f}")

            if not equipamentos:
                print("nada cadastrado")
                return

            total_equipamentos = len(equipamentos)
            soma_valores = sum(item[2] for item in equipamentos)
            media_valor = soma_valores / total_equipamentos

            item_mais_caro = max(equipamentos, key=lambda x: x[2])

            print("\n relatorio")
            print(f"equipamentos cadastrados: {total_equipamentos}")
            print(f"Média de valor: R$ {media_valor:.2f}")
            print(f"Item mais caro: {item_mais_caro[0]} (R$ {item_mais_caro[2]:.2f})")

    except FileNotFoundError:
        print("\nArquivo não encontrado")