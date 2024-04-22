try:
    soma = "10" + 5
    print(soma)
except TypeError: # Exceção do programa
    print("Não tem como somar número com texto, tente novamente")
    
finally:
    print("FIM")  # Aparece de qualquer forma
    
    