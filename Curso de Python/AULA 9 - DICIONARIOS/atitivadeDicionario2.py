# DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.

from time import sleep
from random import randint
from operator import itemgetter

dicionario = {}



player1 = randint(1,6)
player2 = randint(1,6)
player3 = randint(1,6)
player4 = randint(1,6)

for a in range (0,4):
    dicionario['Jogador 1'] = player1
    dicionario['Jogador 2'] = player2
    dicionario['Jogador 3'] = player3
    dicionario['Jogador 4'] = player4
    

    
for k, v in dicionario.items():
    print(f"{k} tirou {v}")

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

for i, n in enumerate(ranking):
    print(f"{i+1}° lugar: {n[0]} com {n[1]}")
    sleep(1)



print(ranking)
print(dicionario)


