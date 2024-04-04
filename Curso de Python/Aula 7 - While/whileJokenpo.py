from random import choice
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
valor = 0
valorFicha = 3

while True:
    escolhaMaquina = choice(opcoes)

    print(escolhaMaquina)


    opcoesUsuario = input("Informe a sua escolha: ").upper()
    print(f"O valor gasto foi de R${valor}")
    
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
        break
    elif escolhaMaquina == "PAPEL" and opcoesUsuario == "TESOURA":
        print(f"A máquina escolheu {escolhaMaquina}, e você {opcoesUsuario} portanto você venceu!")
        break
    elif escolhaMaquina == "PEDRA" and opcoesUsuario == "PAPEL":
        print(f"A máquina escolheu {escolhaMaquina}, e você {opcoesUsuario} portanto você venceu!")
        break


        
    else:
        print(f"A OPÇAO ESTÁ INCORRETA")
        continue
    valor = valor + valorFicha
print(f"Você tem que pagar R${valor + valorFicha}")
