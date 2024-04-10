#DESAFIO 04

#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram o números pares.

lista = []
listaPares = []

for i in range(1,5):
    num = int(input(f"Digite o {i}° número: "))
    lista.append(num)        # Append insere valores em uma lista
    print(lista)
    
    
    resto = num % 2
    if resto == 0:
        listaPares.append(num)
    
    
    

minha_tupla = tuple(lista)
quantidadeNove = minha_tupla.count(9)
posicao3 = tuple.index(3)
numerosPares = tuple(listaPares)

print(f"{minha_tupla}")
print(quantidadeNove)
print(posicao3)
print(numerosPares)

################ ERRO ################

#Segunda Maneira

# numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),\
#             int(input('Digite um número: ')),int(input('Digite um número: ')))

# print(f"O valor 9 apareceu {numeros.count(9)} vezes")
# if 3 in numeros:
#     print(f"O valor 3 está na {numeros.index(3)+1}° posicao")
# else:
#     print(f"O valor 3 não aparece nessa tupla")

# print(f"Os valores pares são ", end='')


# for n in numeros:
#     resto = n % 2
#     if resto == 0:
#         print(n, end=' ')
        
        