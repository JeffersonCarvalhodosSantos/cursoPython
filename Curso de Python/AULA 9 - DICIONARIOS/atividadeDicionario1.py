# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário. No final
# mostre o conteúdo da estrutura na tela.


dicionario = {}

dicionario['nome'] = str(input("Nome: "))
dicionario['nota'] = float(input("Nota: "))

if dicionario['nota'] >= 7:
    dicionario['situacao'] = "Aprovado"
else:
    dicionario['situacao'] = "Reprovado"
print(dicionario)





