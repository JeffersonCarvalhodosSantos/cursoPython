soma = 0 
quantidade = 0
maior = 0
menor = 1000000

while True:
    numeros = int(input("Digite o número: "))
    continua = input("Deseja Continuar? [S/N] ").upper()
    
    quantidade = quantidade + 1
    soma = numeros + soma
    media = soma / quantidade
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
    
    
    
        
        
    if continua == 'N':
        print("Encerrando...")
        break
print(media)
print(maior)
print(menor)