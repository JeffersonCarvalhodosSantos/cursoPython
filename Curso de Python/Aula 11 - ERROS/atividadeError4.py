# DESAFIO 04

# Escreva um programa que peça ao usuário para digitar seu
# nome e idade. Em seguida, exiba uma mensagem
# personalizada que inclua o nome e a idade. Lide com o erro
# caso a idade digitada não seja um número.

try:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    
    
except ValueError:
    print("Digite sua idade com valor numérico...")

else:
    print(f"Cadastro concluído!")