# Problema 1004 - Produto Simples
def produto_simples():
    A = int(input())
    B = int(input())
    PROD = A * B
    print(f"PROD = {PROD}")

# Problema 1005 - Média 1
def media_1():
    A = float(input())
    B = float(input())
    MEDIA = (A * 3.5 + B * 7.5) / 11
    print(f"MEDIA = {MEDIA:.5f}")

# Problema 1011 - Esfera
def esfera():
    R = float(input())
    pi = 3.14159
    volume = (4/3) * pi * (R ** 3)
    print(f"VOLUME = {volume:.3f}")

# Problema 2416 - Corrida
def corrida():
    L = int(input())
    C = int(input())
    resto = L % C
    print(resto)

# Problema 1015 - Distância Entre Dois Pontos
def distancia_entre_pontos():
    import math
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"{distancia:.4f}")

# Problema 1930 - Tomadas
def tomadas():
    T1 = int(input())
    T2 = int(input())
    T3 = int(input())
    T4 = int(input())
    total = (T1 + T2 + T3 + T4) - 3
    print(total)

# Menu para executar os problemas
if __name__ == "__main__":
    print("Escolha o problema para executar:")
    print("1 - Produto Simples (1004)")
    print("2 - Média 1 (1005)")
    print("3 - Esfera (1011)")
    print("4 - Corrida (2416)")
    print("5 - Distância Entre Dois Pontos (1015)")
    print("6 - Tomadas (1930)")
    
    opcao = int(input("Digite o número do problema: "))
    
    if opcao == 1:
        produto_simples()
    elif opcao == 2:
        media_1()
    elif opcao == 3:
        esfera()
    elif opcao == 4:
        corrida()
    elif opcao == 5:
        distancia_entre_pontos()
    elif opcao == 6:
        tomadas()
    else:
        print("Opção inválida!")
