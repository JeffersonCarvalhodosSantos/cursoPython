# Chamar variável que não existe

try:
    print(nome) # Ao não encontrar algo, COMO VARIAVEL OU NOME, ele joga para o EXCEPT
except NameError:
    print("Não tem como chamar variável que não existe, tente novamente...")