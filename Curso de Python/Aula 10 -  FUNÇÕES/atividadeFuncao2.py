# DESAFIO 02

# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.

texto = input("Digite um texto: ")

def escreva(texto):
    quantidade = len(texto)

    print("-" * quantidade)
    print(texto)
    print("-" * quantidade)
    
escreva(texto)



    

