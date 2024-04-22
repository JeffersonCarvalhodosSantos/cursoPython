try:
    divisao = 5 / 0
    print(divisao)
except ZeroDivisionError:
    print("Não há como dividir por Zero, tente novamente...")