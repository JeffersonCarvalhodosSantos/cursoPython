# Break
from random import *
escolhaMaquina = randint(1,20)
print(escolhaMaquina)
ganhei = False


for elemento in range (1,11,1):
    escolhaUsuario = int(input(f"{elemento}ª Rodada, Digite um número: "))

    if escolhaUsuario == escolhaMaquina:
        ganhei = True
        break
    
else:
    print("Maquina venceu")

print("Acabou o jogo, você venceu!")
    
