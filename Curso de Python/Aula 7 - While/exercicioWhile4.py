# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

from random import *
opcoes = ["IMPAR", "PAR"]

vitorias = 0


while True:
    escolhaMaquina = choice(opcoes)
    numeroMaquina = randint(0, 10)
    print(numeroMaquina)
    print(escolhaMaquina)
    
    opcoesUsuario = input("ESCOLHA PAR OU IMPAR: ").upper()
    numeroUsuario = int(input("Escolha um número de 0 a 10: "))

    soma = numeroMaquina + numeroUsuario
    parOuImpar = soma % 2
    
    
    if parOuImpar == 0 and opcoesUsuario == "PAR":
        print(f"Você ganhou, {soma} é par.")
        vitorias = vitorias + 1

    elif parOuImpar == 1 and opcoesUsuario == "IMPAR":
        print(f"Você ganhou, {soma} é ímpar.")
        vitorias = vitorias + 1

    elif parOuImpar == 0 and escolhaMaquina == "PAR":
        print(f"Você perdeu, {soma} é par.")
        break
    
    elif parOuImpar == 1 and escolhaMaquina == "IMPAR":
        print(f"Você perdeu, {soma} é par.")
        break

        
    else:
        print(f"A OPÇAO ESTÁ INCORRETA")
        continue
    
print(f"Você ganhou {vitorias} seguidas.")
