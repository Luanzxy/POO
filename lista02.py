# Questão 1
nome_completo = input("Digite seu nome completo: ")
primeiro_nome = nome_completo.split()[0]
print(f"Bem-vindo(a) ao Python, {primeiro_nome}!")

# Questão 2
x = int(input("Digite a nota do primeiro bimestre da disciplina (0-100): "))
z = int(input("Digite a nota do segundo bimestre da disciplina (0-100): "))
media_parcial = (x * 2 + z * 3) / 5
print(f"Média parcial = {media_parcial:.2f}")

# Questão 3
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2) ** 0.5
print(f"Área = {area:.2f} - Perímetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}")

# Questão 4
frase = input("Digite uma frase: ")
ultima_palavra = frase[frase.rfind(" ") + 1:]
print(ultima_palavra)