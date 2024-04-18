# DESAFIO 08

# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.

# B) A soma dos valores da terceira coluna.

# C) O maior valor da segunda linha.


matriz = [[0,0,0],[0,0,0],[0,0,0]]
c = 0

for i in range(0,3):
    for j in matriz[i]:
        
        if c == 3:
            c = 0
        
        num = int(input(f"Digite um valor para a posição {i},{c}: "))
        matriz[i][c] = num
            
        c += 1
print(matriz)       
for i in range(0,3):
    print(matriz[i])
    i += 1