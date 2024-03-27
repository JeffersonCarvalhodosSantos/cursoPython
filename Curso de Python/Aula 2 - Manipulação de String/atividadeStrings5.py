frase = input("Digite uma frase: ").upper


quantasVezes = frase.count("A")        # Quantas vezes a letra A aparece

qualPosicao = frase.find("A")         # Em que posição ela aparece primeiro

ultimaPosicao = frase.rfind("A")      # Em que posição ela aparece por último

print(f"A letra A apareceu {quantasVezes} vezes")
print(f"A letra A apareceu na {qualPosicao + 1} posição") # Rfind, para contar da direita para a esquerda, e o + 1 pra começar a contar do próximo.
print(f"A letra A apareceu pela última vez {ultimaPosicao + 1} posição")


