from random import choice

opcoes = ["PEDRA" , "PAPEL" , "TESOURA"]
valor = 0
valorFicha = 2

while True:
    escolhaMaquina = choice(opcoes)


    print(escolhaMaquina)

    escolhaUsuario = input("informe a sua escolha: ") . upper()
    #print(f"O valor gasto foi de R$ {valor}")
    if escolhaMaquina ==escolhaUsuario:
        print(f"Ambos escolheu o mesmo {escolhaMaquina}, portanto EMPATE")
       
    elif escolhaMaquina == "PEDRA" and escolhaUsuario == "TESOURA":
        print(f"A maquina escolheu {escolhaMaquina}, portanto ela venceu")

    elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PAPEL":
        print(f"A maquina escolheu {escolhaMaquina}, portanto ela venceu")

    elif escolhaMaquina == "PAPEL" and escolhaUsuario == "PEDRA":
        print(f"A maquina escolheu {escolhaMaquina}, portanto ela venceu")
       
    elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PEDRA":
        print(f"Voce escolheu {escolhaUsuario}, portanto voce venceu")
        break
    elif escolhaMaquina == "PAPEL" and escolhaUsuario == "TESOURA":
        print(f"Voce escolheu {escolhaUsuario}, portanto voce venceu")
        break
    elif escolhaMaquina == "PEDRA" and escolhaUsuario == "PAPEL":
        print(f"Voce escolheu {escolhaUsuario}, portanto voce venceu")
        break
    else:
        print("A opção esta incorreta")
        continue
    valor = valor + valorFicha

print(f"O Valor a pagar R${valor + valorFicha}")