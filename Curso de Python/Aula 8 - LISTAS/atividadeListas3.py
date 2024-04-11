# DESAFIO 03

# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela

# lista = []

# for loop in range (0,6,1):
#     numerosInseridos = int(input(f"Digite o número: "))
#     lista.insert(0, numerosInseridos)
    
    
# listam=max

# print(lista)
    

    
    
    
# print(f"A lista ordenada está assim: {lista}")
############### ESTE FOI DIFERENTE

# lista = []

# for c in range(0,5):
#     numero = int(input("Digite: "))
    
#     if c == 0 or numero > lista[-1]:
#         lista.append(numero)
#         print("Adicionado ao final da lista")
#     else: 
#         pos = 0
#         while pos < len(lista):
#             if numero <= lista[pos]:
#                 lista.insert(pos, numero)
#                 print(f"Adicionado na posição {pos} da lista")
#                 break
#             pos = pos + 1
            
#         print(f"Os valores digitados em ordem foram {lista}")




# ########   Checar comentários no ClassRoom para corrigir   ########### #

####### PROFESSOR >>>>>>>>


lista = []

for c in range(0,5):    
    n = int(input("Digite um valor: "))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1

print(f"Os valores digitados em ordem foram {lista}")