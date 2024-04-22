def numero():
    return 15 # Retorna um valor a sua função

variavelFuncao = numero

print(variavelFuncao() + 5) # É possível salvar funções dentro de uma variável

def calculaPotencia(valor, expoente=2): # Salvar valor fixo dentro da função
    potencia = valor ** expoente
    print(potencia)    
valor = int(input("Digite um valor: "))

calculaPotencia(valor)
    