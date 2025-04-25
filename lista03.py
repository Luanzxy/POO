# Questão 1
A = int(input())
B = int(input())
PROD = A * B
print(f"PROD = {PROD}")



# Questão 2
nota1 = float(input()) * 3.5
nota2 = float(input()) * 7.5
media = (nota1 + nota2) / 11
print(f"MEDIA = {media:.5f}")


# Questão 3
raio = float(input())
pi = 3.14159
volume = (4/3) * pi * (raio ** 3)
print(f"VOLUME = {volume:.3f}")


# Questão 4
import math
x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
dis=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"{dis:.4f}")


# Questão 5
tomadas = list(map(int, input().split()))
quantidade = sum(tomadas) - 3
print(quantidade)


# Questão 6
C, N = map(int, input().split())
quant = C // N
C = C - (N * quant)
print(C)
