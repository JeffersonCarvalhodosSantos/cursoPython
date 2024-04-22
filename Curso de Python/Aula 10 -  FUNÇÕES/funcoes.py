# def Ola():
#     print("Olá, tudo bem?")
#     nome = "Jefferson"


# Ola()
# Ola()
# Ola()
# print(nome)  # Indica erro porque a variável só existe dentro da definição

def calculaArea(largura, altura):  # Para funções sempre iniciar com def, para definir a função e dois ou mais parâmetros.
    area = largura * altura
    print(area)
calculaArea(5,3)

def calculoPerimetro(largura, altura):
    perimetro = (2 * largura) + (2 * altura) # Cálculo do perímetro
    return perimetro   # Devolver um valor para a variável

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

print(calculoPerimetro(5,3))  # Para printar o valor do cálculo
calculoPerimetro(5,3)
calculoPerimetro(largura, altura) # Outra maneira de calcular usando numeros que o usuário digitar