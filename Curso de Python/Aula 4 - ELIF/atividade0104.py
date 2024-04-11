# Desafio 1

valorCasa = float(input("Qual o valor do imóvel? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int(input("Quantos anos deseja pagar? "))
meses = anos * 12

percentualSalario = salario * 0.3      #Calcular o percentual do salário
prestacaoMensal = valorCasa / meses    #Calcular a prestação mensal

if prestacaoMensal > percentualSalario:
     print(f"A prestação mensal é de R$: {prestacaoMensal:.2F}, 30% do seu salário é {percentualSalario:.2F}, portanto o Empréstimo foi negado.") #:.2f para excluir duas casas decimais
else:
     print(f"A prestação mensal é de R$: {prestacaoMensal:.2F}, 30% do seu salário é {percentualSalario:.2F} está dentro do limite, Empréstimo aprovado!")

#Desafio 2

primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))

if primeiroValor > segundoValor:
     print("O Primeiro valor é maior")
elif primeiroValor == segundoValor:
     print("Não existe valor maior, os dois são iguais")
else:
     segundoValor > primeiroValor
     print("O segundo valor é maior")
    
#Desafio 3

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10: 
    if media >= 7:
        print(f"Sua nota média é de: {media}, você está Aprovado!")
    elif media >= 5:
        print(f"Sua nota média é de: {media}, você está em Recuperação!")
    else: 
        media < 5
        print(f"Sua nota média é de: {media}, você está Reprovado!")
else:
    print("Por favor, nos informe a nota correta")

#Desafio 4

anoBase = 2024
anoAtleta = int(input("Digite o ano de seu nascimento: "))

idade = anoBase - anoAtleta

if idade >= 25:
    print(f"Sua idade é: {idade}, sua categoria é MASTER")
elif idade <= 24 and idade > 19:
    print(f"Sua idade é: {idade}, sua categoria é SÊNIOR")
elif idade <= 18 and idade > 14:
    print(f"Sua idade é: {idade}, sua categoria é JUNIOR")
elif idade <= 13 and idade > 9:
    print(f"Sua idade é: {idade}, sua categoria é INFANTIL")
else:
    idade <= 9
    print(f"Sua idade é: {idade}, sua categoria é MIRIM")
    
# #Desafio 5

# retaA = int(input("Digite o tamanho da reta A: "))
# retaB = int(input("Digite o tamanho da reta B: "))
# retaC = int(input("Digite o tamanho da reta C: "))

# somaAB = retaA + retaB
# somaAC = retaA + retaC
# somaBC = retaB + retaC

# if somaAB > retaC and somaAC > retaB and somaBC > retaA:
#     print("Foi possível formar o triângulo!")
# if retaA == retaB and retaB == retaC and retaC == retaA:
#     print("Seu triângulo é Equilátero")
# if retaA == retaB and retaC != retaA and retaC != retaB:
#     print("Seu triângulo é Isósceles")
# if retaA != retaB and retaB != retaC and retaC != retaA:
# else:
    