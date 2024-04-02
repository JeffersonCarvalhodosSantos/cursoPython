#Desafio 2 DESAFIO 02 Escreva um programa que leia dois números inteiros e compare- os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))

if primeiroValor > segundoValor:
     print("O Primeiro valor é maior")
elif primeiroValor == segundoValor:
     print("Não existe valor maior, os dois são iguais")
else:
     segundoValor > primeiroValor
     print("O segundo valor é maior")