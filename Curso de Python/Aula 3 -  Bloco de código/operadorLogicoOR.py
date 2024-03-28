bacalhau = input("Você comprou o bacalhau [S/N] ").upper()
sardinha = input("Você comprou a sardinha [S/N] ").upper()

if bacalhau == "S" or sardinha == "S":
    print("Tem peixe na sexta-feira santa").upper()
else:
    print("Não vai ter peixe na sexta feira santa").upper()