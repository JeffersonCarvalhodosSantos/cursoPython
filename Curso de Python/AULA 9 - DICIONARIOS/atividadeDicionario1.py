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

dados = {}
alunos = list()
pausa = 'N'

while True:
    
    if pausa == 'X':
        break
    else:
        dados['Nome'] = str(input("Nome do aluno: "))
        dados['Media'] = int(input("Media do aluno: "))
        
        if dados['Media'] >= 7:
            dados['situacao']= "Aprovado"
        else:
            dados['situacao']= "Reprovado"
            
       
        alunos.append(dados.copy())
        
    pausa = input('Para continuar digite A para parar digite X:').upper()

print(dados)
for k, v in dados.items():
    print(f"Nome: {k} Situação: {v}")
    print(f"O Nome é igual a {dados['Nome']}")
    print(f"A Média é igual a {dados['Media']}")
    print(f"Sua Situação é {dados['situacao']}")





