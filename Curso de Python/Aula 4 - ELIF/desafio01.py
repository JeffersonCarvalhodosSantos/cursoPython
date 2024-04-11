#DESAFIO 01

#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Qual o valor do imóvel? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int(input("Quantos anos deseja pagar? "))
meses = anos * 12

percentualSalario = salario * 0.3      #Calcular o percentual do salário
prestacaoMensal = valorCasa / meses    #Calcular a prestação mensal

if prestacaoMensal > percentualSalario:
     print(f"A prestação mensal é de R$: {prestacaoMensal:.2F}, 30% do seu salário é {percentualSalario:.2F}, portanto o Empréstimo foi negado.") #:.2f para excluir duas casas decimais
else:
     print(f"A prestação mensal é de R$: {prestacaoMensal:.2F}, 30% do seu salário é {percentualSalario:.2F} está dentro do limite, Empréstimo aprovado!")