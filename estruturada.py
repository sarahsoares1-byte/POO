nomes = []
nota1 = []
nota2 = []

def cadastrar(): 
    nome = input("Digite o nome do aluno: ")
    notas1 = float(input("Digite a primeira nota: "))
    notas2 = float(input("Digite a segunda nota: "))
   

    nomes.append(nome)
    nota1.append(notas1)
    nota2.append(notas2)

    print("Aluno cadastrado com sucesso!")

def calcular_media (indice):
    return (nota1[indice] + nota2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

def listar():
    if len(nomes) == 0:
        print("Nenhum aluno cadastrado.")
        return
    print(f"{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")

    for i in range(len(nomes)):
        print(f"{nomes[i]:<16}{nota1[i]:<7}{nota2[i]:<7}{calcular_media(i):<8.1f}{situacao(i):<14}")

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