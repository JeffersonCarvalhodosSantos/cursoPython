import random

# numeroComputador = random.randint(0,5)
# numeroUsuario = int(input("De 0 a 5, qual número o computador escolheu? "))

# if numeroComputador == numeroUsuario:
#     print(f"Você acertou! o número que o PC escolheu foi {numeroComputador}")
# else:
#     print(f"Você errou! Tente novamente")
    
    
    
# Desafio 2

# velocidade = random.randint(60, 100)
# multa = (velocidade * 7)

# if velocidade > 80:
#     print(f"Você foi multado! A multa vai custar R$ {multa}, dirija com cuidado! ")
# else:
#     print(f"Você está dirigindo dentro do limite!")
    
    
# Desafio 3

# distanciaViagem = float(input("Digite a distância em KM: "))

# if distanciaViagem >= 200:
#     preco = distanciaViagem * 0.50
#     print(f"O preço da passagem será de R$ {preco}")
# else:
#     preco = distanciaViagem * 0.45
#     print(f"O preço da passagem será R$ {preco}")
    
# Desafio 4

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"O maior valor é {n1}")
if n2 > n3 and n2 > n1:
    print(f"O maior valor é {n2}")
if n3 > n2 and n3 > n1:
    print(f"O maior valor é {n3}")
    
if n1 < n2 and n1 < n3:
    print(f"O menor valor é {n1}")
if n2 < n3 and n2 < n1:
    print(f"O menor valor é {n2}")
if n3 < n2 and n3 < n1:
    print(f"O menor valor é {n3}")