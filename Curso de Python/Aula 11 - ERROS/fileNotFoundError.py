try:
    with open("data.txt",  "r") as arquivo:
        conteudo = arquivo.read()
        
except FileNotFoundError:
    print("O arquivo não foi encontrado! Insira o diretório correto...")
except ZeroDivisionError:
    print("Impossível dividir um número por zero")
finally:
    print("FIM")