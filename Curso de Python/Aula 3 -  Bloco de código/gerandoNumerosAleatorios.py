
import random 
from random import randint # importa métodos específicos dentro da biblioteca
# Renomear
import random as rd

nota1 = random.randint(1,10)
nota2 = random.randint(1,10)

media = (nota1 + nota2) / 2   # Parênteses para dar prioridade no operador da matemática

if media >= 7:
    print(f"Você está Aprovado(a)")
else:
    print(f"Você foi Reprovado(a)")

