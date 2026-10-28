import json

def definir_nivel(valor):
    if valor < 50:
        return "precisa de troca"
    elif 50 <= valor <= 79:
        return "normal"
    else:
        return "muito bom"

def buscar_equipamento():
    termo_busca = input("Digite o nome: ").strip().lower()

    try:
        with open('equipamentos.json', 'r', encoding='utf-8') as arquivojson:
            equipamentos = json.load(arquivojson)

        encontrado = False

        for item in equipamentos:
            nome = item.get('nome', '')
            if nome.lower() == termo_busca:
                patrimonio = item.get('idade', item.get('patrimonio', 'N/A'))
                valor = float(item.get('pontuacao', item.get('valor', 0)))
                estado = definir_nivel(valor)

                print("\n equipamento encontrado")
                print(f"Nome: {nome}")
                print(f"Patrimônio: {patrimonio}")
                print(f"Valor: R$ {valor:.2f}")
                print(f"Estado: {estado}")
                encontrado = True
                break

        if not encontrado:
            print(f"\n'{termo_busca}' não foi encontrado")

    except:
        return []