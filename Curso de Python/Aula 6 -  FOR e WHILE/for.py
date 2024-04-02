# FOR - Quando sabemos o limite/fim
# WHILE - Quando não sabemos o fim/limite

              # Explicação

# limite < 10 peças - para que ele continue rodando até chegar ao 10.

inicio = 0
fim = 11
salto = 1  # Se não houver variável salto, ou número 0 o programa entende como 1.


for peca in range (inicio, fim, salto):
    print(peca)
else:
    print("as peças foram finalizadas")