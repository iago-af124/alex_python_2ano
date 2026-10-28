alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota principal: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

cadastrar_aluno()
print(alunos)
