numero = int(input("Digite um valor: "))

resto = numero % 2 # Porcentagem captura o resto da divisão
# print(resto)
if resto == 0:
    print(f"O valor {numero} é PAR")
else:
    print(f"O valor {numero} é IMPAR")