from random import *
escolhaMaquina = randint(0,10)
print(escolhaMaquina)
rodadas = 0  # Variável declarando o início de jogadas

while True:

    escolhaUsuario = int(input("Escolha um número: "))
    rodadas = rodadas + 1
    if escolhaUsuario == escolhaMaquina:
        print(f"A máquina escolheu {escolhaMaquina} e você escolheu {escolhaUsuario}, portanto você venceu! Após {rodadas} tentativas.")
        break
    print("Continue escolhendo...")
            
        
        
        
        

    
    
        
               
            