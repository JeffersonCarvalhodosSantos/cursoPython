# Capturando a sétima letra (Toda string começa do '0')
frase = "CURSO DE PYTHON"

setimaLetraFrase = frase[6]

print(setimaLetraFrase)

# Capturando a oitava letra do meu nome
nome = "Jefferson Carvalho"

oitavaLetraNome = nome[7]
print(oitavaLetraNome)

# Capturando uma secção    

print(frase[9:15]) # (quando for a última letra, adicionar mais um número, pois ele não reconhece a última como a última)

print(frase[:5]) # Acrescendo um ao final.

print(frase[9:]) # Com os dois pontos automaticamente ele reconhece que tem que ir até o final

print(nome[10:18])

### Pulando caracteres

print(frase[9:15:2])  # Terceiro parâmetro como salto (com dois pontos) ou deixar o do meio vazio.



  
