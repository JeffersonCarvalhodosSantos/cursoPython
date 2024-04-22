# DESAFIO 01

# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.



comprimento = int(input("Digite o comprimento do terreno: "))
largura = int(input("Digite a largura do terreno: "))


def area(comprimento, largura):
    perimetro = (comprimento * largura)
    return perimetro

print(f"A área do terreno é igual a {area(comprimento, largura)} m²")

