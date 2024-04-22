# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário. No final
# mostre o conteúdo da estrutura na tela.


# dicionario = {}

# dicionario['nome'] = str(input("Nome: "))
# dicionario['nota'] = float(input("Nota: "))

# if dicionario['nota'] >= 7:
#     dicionario['situacao'] = "Aprovado"
# else:
#     dicionario['situacao'] = "Reprovado"
# print(dicionario)

alunos = []

while True:
    dados = {}
    
    dados['Nome'] = input("Nome do aluno: ")
    dados['Media'] = float(input("Média do aluno: "))
    
    if dados['Media'] >= 7:
        dados['Situacao'] = "Aprovado"
    elif dados['Media'] >= 5:
        dados['Situacao'] = "Recuperação"
    else:
        dados['Situacao'] = "Reprovado"

    alunos.append(dados)
    
    pausa = input('Para continuar digite S, para parar digite X: ').upper()
    if pausa == 'X':
        break

for aluno in alunos:
    print(f"\nNome: {aluno['Nome']}")
    print(f"Média: {aluno['Media']}")
    print(f"Situação: {aluno['Situacao']}")





