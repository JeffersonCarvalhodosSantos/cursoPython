#DESAFIO 03

#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
#do Campeonato Brasileiro Serie B de Futebol, na ordem de
#colocação. Depois mostre:

#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time do Santos.

classificacao = ['Amazonas FC' , 'América-MG' , 'Avai' , 'Botafogo SP' , 'Brusque' , 'CRB' , 'Ceará' , 'Chapecoense' , 'Coritiba' , 'Goiás' , 'Guarani' , 'Ituano' , 'Mirassol' , 'Novorizontino' , 'Operário' , 'Paysandu' , 'Ponte Preta' , 'Santos' , 'Sport' , 'Vila Nova']

cincoPrimeiros = classificacao[0:4]
print(cincoPrimeiros)

serieC = classificacao[16:20]
print(serieC)

ordemAlfabetica = sorted(classificacao)
print(ordemAlfabetica)

santosJaVaiCair = classificacao[17]
print(santosJaVaiCair)



