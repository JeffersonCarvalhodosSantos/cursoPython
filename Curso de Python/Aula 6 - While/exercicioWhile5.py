deMaior = 0
homens = 0
mulheres = 0


while True:

    idade = int(input("Qual a idade? "))
    sexo = input("Qual o sexo? M ou F? ").upper()  # Colocar controle Regrar F ou M
    continuar = input("Deseja continuar cadastrando? [S/N]").upper()

    if idade >= 18:
        deMaior = deMaior + 1
    else: deMaior = deMaior  # Não precisa ser feito (testar)

    if sexo == "M":
        homens = homens + 1
    else: homens = homens

    if idade <= 20 and sexo == "F":
        mulheres = mulheres + 1
    else: mulheres = mulheres

    if continuar == "N":
        break

    print(f"De maior: {deMaior}")
    print(f"Homens: {homens}")
    print(f"Mulheres com menos de 20: {mulheres}")