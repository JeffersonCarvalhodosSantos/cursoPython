nome = input("Digite seu nome completo: ")

nomeMaiusculo = print(nome.upper()) # Nome com todas as letras maiúsculas

nomeMinusculo = print(nome.lower()) # Nome com todas as letras minúsculas

dividirNome = nome.split()

nomeSemEspaco = nome.replace(" " , "")

print(dividirNome)

print(nomeSemEspaco)

print(nomeMaiusculo)  # Nome maiúsculo
print(nomeMinusculo)  # Nome minúsculo
print(len(nomeSemEspaco)) # Quantas letras ao todo sem espaços
print(len(dividirNome[0])) # Quantas letras tem o primeiro nome




