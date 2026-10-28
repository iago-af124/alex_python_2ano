def historico():
    try:
        with open("equipamentos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        registros = []
        for linha in linhas:
            linha_limpa = linha.strip()
            
            if linha_limpa:
                partes = linha_limpa.split()
                
                if len(partes) >= 2:
                    nome = partes[0]
                    try:
                        valor = float(partes[1])
                        registros.append((nome, valor))
                    except:
                        continue

        registros.sort(key=lambda x: x[1], reverse=True)

        print("\n historico")
        posicao = 1
        for nome, valor in registros:
            print(f"{posicao} - {nome} - R$ {valor:.2f}")
            posicao += 1

        print(f"registros validos: {len(registros)}")

    except FileNotFoundError:
        print("\n'equipamentos.txt' nao foi criado")