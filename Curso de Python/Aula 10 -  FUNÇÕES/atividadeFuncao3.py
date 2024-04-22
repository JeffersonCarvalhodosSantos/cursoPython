# DESAFIO 03

# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))

def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return f"O número {n1} é o maior valor"  # No RETURN, Podemos inserir o texto dessa maneira, semelhante ao print
    elif n2 > n3:
        return f"O número {n2} é o maior valor"
    else:
        return f"O número {n3} é o maior valor"
    
print(maior(v1, v2, v3))