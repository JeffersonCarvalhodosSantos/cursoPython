# DESAFIO 04

# Crie um programa que vai ler vários números e colocar em
# uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaPar = []
listaImpar = []


while True:

    for i in range(0,10):
        numero = int(input("Digite um número: "))
        lista.append(numero)
        print(lista)
        
    resto = numero % 2


    if resto == 0:
        listaPar.append(numero)
        
    elif resto == 1:
        listaImpar.append(numero)
        break