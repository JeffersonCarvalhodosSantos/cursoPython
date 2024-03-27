nomeCompleto = input("Digite seu nome completo: ")

print(nomeCompleto.split())  # Separa os nomes

primeiroNome = nomeCompleto.split()
ultimoNome = nomeCompleto.split()


print(primeiroNome[0], ultimoNome[-1])  # Mostra o primeiro e o último nome
