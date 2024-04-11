# # DESAFIO 07

# # Crie um programa que cria uma matriz de dimensão 3x3 e
# # preencha com valores lidos pelo teclado.

# No final mostre a Matriz na tela, com a formatação correta.


matriz = [[0,0,0],[1,1,1],[2,2,2]]

c=0                      # Contagem

for i in range (0,3):    # percorre cada lista dentro da matriz.

    for j in matriz[i]:  # para cada espaço dentro da lista da matriz, se C for igual a 3, passa a ser 0
        if c==3:
            c=0
        inserirMatriz = int(input(f"Insira um valor para[{i}, {c}]: "))

        matriz[i][c] = inserirMatriz
        c = c + 1



print(matriz[0]) # Primeira lista
print(matriz[1]) # Segunda lista
print(matriz[2]) # Terceira lista


