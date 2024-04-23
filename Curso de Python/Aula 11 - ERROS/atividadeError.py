# DESAFIO 01

# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.

#Podemos usar while e break para repetir a cada vez que o usuário errar algo.

try:
    
    numUsuario = int(input("Digite um número: "))
    numUsuario2 = int(input("Digite outro número: "))
    divisao = numUsuario / numUsuario2

    if numUsuario == 0 and numUsuario2 == 0:
        print("Não será possível fazer a divisão, alguém escolheu o número '0'")
    else: numUsuario and numUsuario2 != 0
    print(divisao)
    
except ZeroDivisionError:
    print("Não há como dividir por Zero, tente novamente...")
    
except ValueError:
    print("Digite um valor numérico")