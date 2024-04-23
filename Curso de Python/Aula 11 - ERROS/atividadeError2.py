# DESAFIO 02

# Escreva um programa que leia um arquivo de texto chamado
# "dados.txt" e exiba seu conteúdo. Certifique-se de lidar com o
# erro caso o arquivo não exista.

try:
    with open("dados.txt",  "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        
except FileNotFoundError:
    print("O arquivo não foi encontrado! Insira o diretório correto...")

finally:
    print("FIM")