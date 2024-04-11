# dicionario = {

# "Nome": "Jeff",

# "Sobrenome": "Carvalho",

# "Idade": 30

# }


# print(dicionario)            # Acessando um dicionário
# print(dicionario.items())    # Itens de um dicionário
# print(dicionario.keys())     # Chaves de um dicionário
# print(dicionario.values())   # Valores de um dicionário



######################### LISTA DE DICIONÁRIOS ###########################

# personagem =[
#     {
#         "Nome": "Bob",
#         "Sobrenome": "Esponja",
#         "Idade": 10    
#     },
    
#     {
#         "Nome": "Johnny",
#         "Sobrenome": "Bravo",
#         "Idade": 35
        
#     },
    
#     {
#         "Nome": "Chaves",
#         "Sobrenome": "do Oito",
#         "Idade": 8
#     }
    
# ] 

# print(personagem[0]) # Acessa o primeiro item e assim sucessivamente...
# print(personagem[0].get("Nome")) # Outra maneira de aparecer o valor específico dentro do item
# print(personagem["Nome"]) # Acessa o valor dentro do item


############################ PERCORRENDO ITENS COM for ##################################

estado = {}
brasil = list() # Podemos declarar lista dessa maneira

for c in range(0,2):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
    
print(brasil)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print