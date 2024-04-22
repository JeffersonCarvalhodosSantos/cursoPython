try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número, por favor, digite um número...")
else:    # Diferente do finally, que é executado de qualquer forma ao final do código, o else só é executado quando o código for corretamente...
    print(numero)
    
