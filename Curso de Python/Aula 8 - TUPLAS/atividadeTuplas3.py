#DESAFIO 03

#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
#do Campeonato Brasileiro Serie B de Futebol, na ordem de
#colocação. Depois mostre:

#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time do Santos.

classificacao = ['Amazonas FC' , 'América-MG' , 'Avai' , 'Botafogo SP' , 'Brusque' , 'CRB' , 'Ceará' , 'Chapecoense' , 'Coritiba' , 'Goiás' , 'Guarani' , 'Ituano' , 'Mirassol' , 'Novorizontino' , 'Operário' , 'Paysandu' , 'Ponte Preta' , 'Santos' , 'Sport' , 'Vila Nova']

cincoPrimeiros = classificacao[0:5]
print(f"Os times {cincoPrimeiros} são os cinco primeiros da tabela")

serieC = classificacao[16:20]
print(f"Os times {serieC} são os 4 últimos da tabela") 

ordemAlfabetica = sorted(classificacao)
print(f"A Classificação em ordem alfabética: {ordemAlfabetica}")  # Sorted

santosJaVaiCair = classificacao[17]
print(f"Mal começou e o {santosJaVaiCair} já vai cair em 17° kkkk")



