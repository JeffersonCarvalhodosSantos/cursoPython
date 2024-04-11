#Desafio 4
#A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.

from datetime import *  # Asterisco para importar todas os métodos


dataAtual = date.today()
anoAtual = dataAtual.year
mesAtual = dataAtual.month
diaAtual = dataAtual.day


anoAtleta = int(input("Digite o ano de seu nascimento: "))

idade = anoAtual - anoAtleta


if idade >= 25:
    print(f"Sua idade é: {idade}, sua categoria é MASTER")
elif idade <= 24:
    print(f"Sua idade é: {idade}, sua categoria é SÊNIOR")
elif idade <= 18:
    print(f"Sua idade é: {idade}, sua categoria é JUNIOR")
elif idade <= 13:
    print(f"Sua idade é: {idade}, sua categoria é INFANTIL")
else:
    idade <= 9
    print(f"Sua idade é: {idade}, sua categoria é MIRIM")