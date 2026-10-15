class estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        elif self.media() >= 4:
            return "Recuperação"
        return "Reprovado"

def descrever(self):
    return f"{self.nome:<16}{self.nota1:<7}{self.nota2:<7}{self.media():<8.1f}{self.situacao():<14}"

estudantes = []

def cadastrar(): 
    nome = input("Digite o nome do aluno: ")
    notas1 = float(input("Digite a primeira nota: "))
    notas2 = float(input("Digite a segunda nota: "))

    estudantes.append(estudante(nome, notas1, notas2))
    print("Aluno cadastrado com sucesso!")

def listar():
    if len(estudantes) == 0:
        print("Nenhum aluno cadastrado.")
        return
    print(f"{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")

    for estudante in estudantes:
        print(estudante.descrever())

def menu():
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

menu()
