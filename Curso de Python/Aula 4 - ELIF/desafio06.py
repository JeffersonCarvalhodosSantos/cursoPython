#Crie um programa que faça o computador jogar Jokenpô com você:

from random import choice

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

escolhaMaquina = choice(opcoes)
print(escolhaMaquina)


opcoesUsuario = input("Informe a sua escolha: ").upper()

if opcoesUsuario == escolhaMaquina:
    print(f"Ambos escolheram {escolhaMaquina}, portanto deu empate!")

elif escolhaMaquina == "PEDRA" and opcoesUsuario == "TESOURA":
    print(f"A Máquina escolheu {escolhaMaquina}, portanto ela venceu!")
elif escolhaMaquina == "TESOURA" and opcoesUsuario == "PAPEL":
    print(f"A máquina escolheu {escolhaMaquina}, portanto ela venceu!")
elif escolhaMaquina == "PAPEL" and opcoesUsuario == "PEDRA":
    print(f"A máquina escolheu {escolhaMaquina}, portanto ela venceu!")
    
elif escolhaMaquina == "TESOURA" and opcoesUsuario == "PEDRA":
    print(f"A máquina escolheu {escolhaMaquina}, e você {opcoesUsuario} portanto você venceu!")
elif escolhaMaquina == "PAPEL" and opcoesUsuario == "TESOURA":
    print(f"A máquina escolheu {escolhaMaquina}, e você {opcoesUsuario} portanto você venceu!")
elif escolhaMaquina == "PEDRA" and opcoesUsuario == "PAPEL":
    print(f"A máquina escolheu {escolhaMaquina}, e você {opcoesUsuario} portanto você venceu!")


    
else:
    print(f"A OPÇAO ESTÁ INCORRETA")
