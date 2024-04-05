soma = 0
condicaoDeParada = 999

while True:
    numeros = int(input("Digite um número: "))
    if numeros == condicaoDeParada:
        print("Parando...")
        print(f"A Soma dos números digitados é {soma}")
        break
    soma = numeros + soma
    
    
