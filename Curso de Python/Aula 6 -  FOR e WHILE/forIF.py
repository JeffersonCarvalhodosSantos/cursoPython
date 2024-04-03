from random import *


maquina = usuario = 0



for elemento in range (1,11):
    escolhaMaquina = randint(0,5)
    numero = int(input(f"{elemento}ª Rodada, Digite um número: "))
    print(escolhaMaquina)
    
    
    if numero == escolhaMaquina:
        print(f"A máquina escolheu {escolhaMaquina}, você acertou!")
        #usuario = usuario + 1
        usuario += 1
    else:
        print(f"A máquina escolheu {escolhaMaquina}, você errou!")
        maquina = maquina + 1
        
else: 
    
    if usuario > maquina:
        print("Usuário venceu!")
    elif usuario == maquina:
        print("Empate!")
    else:
        print("A máquina venceu!")
