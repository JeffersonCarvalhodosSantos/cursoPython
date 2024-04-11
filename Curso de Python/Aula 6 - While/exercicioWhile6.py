compraTotal = 0
produtosMaiores = 0 
produtoMaisBarato = 100000000000
produtoMaisBarato = 0


while True:

    nomeProduto = input("Digite o nome do produto: ").upper
    preco = float(input("Digite o preço: "))
    continuar = input("Deseja continuar cadastrando? [S/N]")
    compraTotal = compraTotal + preco
    
    if preco > 100:
        produtosMaiores += 1
    else: produtosMaiores = produtosMaiores
    
    if preco < produtoMaisBarato:
        produtoMaisBarato = preco
        produtoMaisBarato
        
        
        
    #  (!)   # REVISAR O CÓDIGO... (!)