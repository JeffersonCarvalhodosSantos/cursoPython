# DESAFIO 05

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
#de mostrar que tipo de triângulo será formado:

#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

retaA = int(input("Digite o tamanho da reta A: "))
retaB = int(input("Digite o tamanho da reta B: "))
retaC = int(input("Digite o tamanho da reta C: "))

somaAB = retaA + retaB
somaAC = retaA + retaC
somaBC = retaB + retaC

if somaAB > retaC and somaAC > retaB and somaBC > retaA:
    if retaA == retaB == retaC:
        print("O Triângulo formado foi o Equilátero")
    elif retaA != retaB != retaC != retaA:
        print("O triângulo formado foi o Escaleno")
    else:
        print("O triângulo formado foi o Isósceles") 
else:
    print("Não foi possível formar o triângulo!")