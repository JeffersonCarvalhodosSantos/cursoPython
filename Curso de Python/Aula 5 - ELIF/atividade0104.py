# Desafio 1

# valorCasa = float(input("Qual o valor da casa? "))
# salario = float(input("Qual o valor do seu salário? "))
# anos = float(input("Quantos anos deseja pagar? "))
# meses = anos * 12

# percentualSalario = salario * 0.3     # Calcular o percentual do salário
# prestacaoMensal = valorCasa / meses   # Calcular a prestação mensal

# if percentualSalario <= 30:
#     print(f"O Valor R$ {percentualSalario}, excede o limite, o Empréstimo foi negado.")
# else:
#     print(f"O Valor R$ {percentualSalario}, está dentro do limite, Empréstimo aprovado!")


# Desafio 2

# primeiroValor = int(input("Digite o primeiro valor: "))
# segundoValor = int(input("Digite o segundo valor: "))

# if primeiroValor > segundoValor:
#     print("O Primeiro valor é maior")
# elif primeiroValor == segundoValor:
#     print("Não existe valor maior, os dois são iguais")
# else:
#     segundoValor > primeiroValor
#     print("O segundo valor é maior")
    
# Desafio 3

# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input("Digite sua segunda nota: "))

# media = (nota1 + nota2) / 2

# if media >= 7:
#     print(f"Sua nota média é de: {media}, você está Aprovado!")
# elif media > 5 and media < 7:
#     print(f"Sua nota média é de: {media}, você está em Recuperação!")
# else: 
#     media < 5
#     print(f"Sua nota média é de: {media}, você está Reprovado!")


# Desafio 4

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
    
# Desafio 5
