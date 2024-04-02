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
    
else:
    print(f"A máquina escolheu {escolhaMaquina}, portanto você venceu!")
