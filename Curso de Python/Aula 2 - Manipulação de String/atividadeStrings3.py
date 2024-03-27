nomeCidade = input("Digite o nome de uma cidade: ").upper  # Tirar o problema do usuario digitar de qualquer jeito


print(nomeCidade.find("Santo"))

primeiroNomeCidade = nomeCidade.split()


print("Santo" in primeiroNomeCidade[0])

print(primeiroNomeCidade[0])