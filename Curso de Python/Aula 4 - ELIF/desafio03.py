# DESAFIO 03 Crie um programa que leia duas notas entre 0 a 10 de um aluno
#e calcule sua média, mostrando uma mensagem no final, de
#acordo com a média atingida.

#Média abaixo de 5.0: REPROVADO

#Média entre 5.0 a 6.9: RECUPERAÇÃO

#Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:  # Linha para o usuário não digitar valores fora dos padrões estabelecidos
    if media >= 7:
        print(f"Sua nota média é de: {media}, você está Aprovado!")
    elif media >= 5:
        print(f"Sua nota média é de: {media}, você está em Recuperação!")
    else: 
        media < 5
        print(f"Sua nota média é de: {media}, você está Reprovado!")
else:
    print("Por favor, nos informe a nota correta")