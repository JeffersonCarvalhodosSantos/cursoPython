#DESAFIO 02

#Crie um programa que vai gerar cinco números aleatórios e colocar
#em uma tupla.

#Depois disso, mostre a listagem de números gerados e também
#indique o menor e o maior valor que estão na Tupla.


from random import randint
import random

for numeroAleatorio in range (0,5):
        numeroAleatorio = random.randint(5,15)
        
        tupla = tuple(numeroAleatorio) 
print(numeroAleatorio)



        

        


 

