from random import randint


maquina = 0
usuario = 0



for elemento in range (1,11):
    numero = int(input(f"{elemento}ª Rodada, Digite um número: "))
    aleatorio = randint(0,5)
    
    if numero == aleatorio:
        print("Você acertou!")
        usuario = usuario + 1
    else:
        print("Você errou!")
        maquina = maquina + 1
