#DESAFIO 05

#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.

#No final, mostre uma listagem de preços, organizando os dados em
#forma tabular.


# Biblioteca Tabulate

produtos = ("Notebook", 3000.00, "Pen Drive", 100.00, "SSD 2TB", 500.00, "Monitor 20'", 1500.00, "Teclado", 250.00)
tamanho = len(produtos)

for i in range (0, tamanho, 2):
    print(f"{produtos[i]:.<30}....R${produtos[i + 1]}")




######################### Outra forma
# ##**********MODO 2**********
# #No terminal( para instalar a biblioteca): pip install tabulate

# from tabulate import tabulate

# produtos = [["Bala","0.30"],["suco","4.10"],["Sorvete","32.30"],["Paçoca","1.5"],["MeM","11.30"],["Milka","18.30"]]

# tpProduto = tuple(produtos)
           
# print(tabulate(tpProduto, headers=["Produto", "Preço"]))