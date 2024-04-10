#DESAFIO 02

#Crie um programa que vai gerar cinco números aleatórios e colocar
#em uma tupla.

#Depois disso, mostre a listagem de números gerados e também
#indique o menor e o maior valor que estão na Tupla.


from random import randint
import random

maior = 0
menor = 0
lista = []

for numero in range (0,5):
        
        numeroAleatorio = random.randint(5,15)
        lista.append(numeroAleatorio)
        

### Transformar a TUPLA em LISTA ### 
        
print(lista)



# # ###### ### #### ### # Segunda maneira 


# n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)

# print('os valores sorteador foram: ', end=' ')


# for numeros in n:
#         print(f"{numeros}", end=' ')  # END= -  Adiciona sempre um caractere ao final de cada print nele mencionado, e mantém na mesma linha
        
# print(f"\nO maior valor sorteado foi {max(n)}")
# print(f"O menor valor sorteado foi {min(n)}")   # Min e max já identifica qual é o menor e qual o maior, substituindo os IF'S e ELSE'S


        

        


 

