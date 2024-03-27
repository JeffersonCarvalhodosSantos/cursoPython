frase = "Microsoft Power BI"

# Trocando uma palavra
trocaPalavra = frase.replace("Power BI" , "AZ-900")
print(trocaPalavra)

# Converter todas as letras para maiúscula
print(frase.upper())


# Converter todas as letras para minúscula
print(frase.lower())

# Converter a primeira letra da frase maiúscula
print(frase.capitalize())

# Converter a primeira letra de cada palavra da frase
print(frase.title())

# Excluir os espaçamentos em excesso da frase
cursoEspacado = "                                                       Fundamentos da Ciências de Dados - Google Cloud                         "

removeEspacoCurso = cursoEspacado.strip()

print(removeEspacoCurso)

# Excluir o espaçamento da direita
cursoEspacado = "                                                       Fundamentos da Ciências de Dados - Google Cloud                         "

removeEspacoCurso = cursoEspacado.rstrip()

print(removeEspacoCurso)

# Excluir o espaçamento da esquerda
cursoEspacado = "                                                       Fundamentos da Ciências de Dados - Google Cloud                         "

removeEspacoCurso = cursoEspacado.lstrip()

print(removeEspacoCurso)


