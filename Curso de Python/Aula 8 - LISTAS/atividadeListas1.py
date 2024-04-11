# DESAFIO 01

# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista. 


lista = []


for i in range (1,6):
    numerosInseridos = int(input(f"Digite o {i}° número: "))
    lista.append(numerosInseridos)
    print(lista)
    
    
maximo = max(lista)
minimo = min(lista)    
  

print(f"\nO maior número digitado foi {max(lista)} que está na posição {lista.index(maximo)}" , end=' ')
print(f"\nO menor número digitado foi {min(lista)} que está na posição {lista.index(minimo)}" , end=' ')   # Lista Index para determinar a posição do valor