import csv
import json

def load_json():
    try:
        with open('equipamentos.json', 'r', encoding='utf-8') as arquivojson:
            return json.load(arquivojson)
    except:
        return []

def add_json(dado):
    with open('equipamentos.json', 'w', encoding='utf-8') as arquivojson:
        json.dump(dado, arquivojson, indent=4, ensure_ascii=False)

def adicionar():
    nome = input('Nome: ').strip()
    patrimonio = input('Patrimônio: ').strip()
    valor = float(input('Valor: '))

    with open('equipamentos.txt', 'a', encoding='utf-8') as arquivotxt:
        arquivotxt.write(f"{nome} {valor}\n")

    with open('equipamentos.csv', 'a', newline='', encoding='utf-8') as arquivocsv:
        escritor = csv.writer(arquivocsv)
        escritor.writerow([nome, patrimonio, valor])

    dados = load_json()
    novo_equipamento = {
        "nome": nome,
        "idade": patrimonio,
        "pontuacao": valor
    }
    dados.append(novo_equipamento)
    add_json(dados)

    print("\nequipamento cadastrado")