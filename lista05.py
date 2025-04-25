# Questão 1
def maior(x, y):
    return x if x > y else y

def maior_entre_dois():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(f"O maior número é: {maior(x, y)}")

# Questão 2
def maior(x, y, z):
    return max(x, y, z)

def maior_entre_tres():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    z = float(input("Digite o terceiro número: "))
    print(f"O maior número é: {maior(x, y, z)}")

# Questão 3
def iniciais(nome):
    return ''.join([parte[0].upper() for parte in nome.split()])

def obter_iniciais():
    nome = input("Digite seu nome completo: ")
    print(f"As iniciais do nome são: {iniciais(nome)}")

# Questão 4
def aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media >= 60

def situacao_aluno():
    nota1 = float(input("Digite a nota do primeiro bimestre: "))
    nota2 = float(input("Digite a nota do segundo bimestre: "))
    if aprovado(nota1, nota2):
        print("Aluno aprovado!")
    else:
        print("Aluno em prova final!")

# Questão 5
def formatar_nome(nome):
    return nome.title()

def formatar_nome_usuario():
    nome = input("Digite seu nome: ")
    print(f"Nome formatado: {formatar_nome(nome)}")

# Questão 6
if __name__ == "__main__":
    print("Escolha o exercício para executar:")
    print("1 - Maior entre dois números")
    print("2 - Maior entre três números")
    print("3 - Iniciais do nome")
    print("4 - Situação do aluno")
    print("5 - Formatar nome")

    opcao = int(input("Digite o número do exercício: "))

    if opcao == 1:
        maior_entre_dois()
    elif opcao == 2:
        maior_entre_tres()
    elif opcao == 3:
        obter_iniciais()
    elif opcao == 4:
        situacao_aluno()
    elif opcao == 5:
        formatar_nome_usuario()
    else:
        print("Opção inválida!")
