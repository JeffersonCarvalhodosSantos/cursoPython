# DESAFIO 03

# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso o CTPS for diferente de ZERO, o
# dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a
# pessoa vai se aposentar.

# Sabendo que ele vai se aposentar após 35 anos de
# colaboração.

from datetime import date

dicionario = {}
anoAtual = date.year

dicionario['nome'] = str(input("Nome: "))
dicionario['ano'] = int(input("Nascimento: "))
dicionario['carteira'] = int(input("Carteira de trabalho: "))


idade = (anoAtual - dicionario['ano'])
del dicionario['ano']
dicionario['Idade'] = idade

if dicionario['carteira'] == 0:
    print(dicionario)
    for k, v in dicionario.items():
        print(f" O {k} tem o valor {v}")
        
        
# falta colocar se caso não tenha carteira
        
        


print(dicionario)



