# DESAFIO 03

# Escreva um programa que solicite ao usuário para digitar um
# número inteiro e exiba o resultado da sua raiz quadrada. Lide
# com o erro caso o número seja negativo.

from math import sqrt    # Importar a biblioteca matemática para calculo raiz quadrada
 
try:
        
    num = int(input("Digite um número inteiro para descobrir sua raíz quadrada: "))
    resultado = sqrt(num)
   
except ValueError:
    print("Por favor, digite um valor numérico positivo...") 
    
else:
    print(resultado)