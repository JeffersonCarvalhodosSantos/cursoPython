# DESAFIO 02

# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente.

# lista = []

# while True:

# # Checar comentários no ClassRoom para corrigir

# if numero i in range (1,3):
#         numerosInseridos = int(input(f"Digite o {i}° número: "))
#         lista.append(numerosInseridos)

# if numerosInseridos == numerosInseridos:
#     numerosInseridos.remove(numerosInseridos)
#     print(numerosInseridos)

        




    
    
    
# print(f"Os valores em ordem crescente são: {sorted(lista)}")



lista = []

while True:

    numero = str(input('Digite um valor para adicionar em uma lista e N para parar: '))

    if numero.upper() == 'N':
        break

   
    if int(numero) in lista:
        print(f'O numero {int(numero)} ja foi adicionado')

    else:
        lista.append(int(numero))

lista.sort()

print(f"Os valores digitados em ordem crescente foram {lista}")

