# DESAFIO 05

# Faça um programa que leia nome e peso de varias pessoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Um listagem com as pessoas mais leves

lista = []
pessoas_cadastradas = 0

while True:
    
    nome_usuario = input("Digite o nome da pessoa: ").upper()
    lista.append(nome_usuario)
    pessoas_cadastradas = pessoas_cadastradas + 1
    
    peso_usuario = float(input("Digite o peso da pessoa: ")) 
    lista.append(peso_usuario)
    continuar = input("Deseja continuar? S ou N: ").upper()
    
    if continuar == "N":
        break
    
print(f"Foram cadastradas {pessoas_cadastradas} pessoas.")
print(lista)