# # Desafio 1

import time

inicio = 10
fim = -1
salto = -1


for elemento in range (inicio, fim, salto):
    time.sleep(1)
    print(elemento)
else: print("Estouro dos fogos!")



# Desafio 2

inicio = 50
fim = 1

for elemento in range (inicio, fim, -2):
    
 
    print(elemento)
    

    
# Desafio 3
inicio = 1
fim = 500
soma = 0

for elemento in range (inicio, fim, 1): # Elemento são tudo que está dentro do range
    impar = elemento % 2                # Para descobrir o número impar
    multiplo3 = elemento % 3            # Para descobrir o número múltiplo de 3
    if impar != 0 and multiplo3 == 0:   # Se impar for diferente de 0 e multiplo de 3 for igual a 0
        print(f"O número {elemento} é impar e múltiplo de 3")
        soma = soma + elemento
print(f"A soma de todos os valores impares e múltiplos de 3 é {soma}")



# # Desafio 4

numero = int(input("Escolha um número: "))
for elemento in range (1,11,1):
    resultado = elemento * numero
    print(f"{numero} X {elemento} = {resultado}")



# Desafio 5

for elemento in range (1,7,1):
    numeroInteiro = int(input("Digite um número: "))
    impar = elemento % 2
    
        
    print(numeroInteiro)

Outra forma de resolver o desafio 5

soma = 0 

for elemento in range (1, 7):
    numero = int(input(f"Digite o {elemento}° valor: "))
    
    resto = numero % 2
    
    if resto  == 0:
        soma = soma + numero 
else:
    print(f"A soma dos valores pares digitados foi igual a: {soma}")
    
    
    
    
# Desafio 6

primeiroTermo = int(input("Termo: "))
razao = int(input("Razão: "))

ultimoTermo = (primeiroTermo + (10-1) * razao) + razao   # Equação de Progressão Aritimética

for elemento in range (primeiroTermo, ultimoTermo, razao):
    print(elemento, end=' -> ')    # END junta os dois prints na mesma linha
else:
    print("Fim!")