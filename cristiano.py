titulos = int(input("Informe a quantidade de títulos que o Cristiano Ronaldo tem: "))
print("\n")
superCopaDePortugal= int(input("Tírulos da Super Copa de Portugal: "))
premierLeague = int(input("Títulos de Premier League: "))
faCup = int(input("Títulos de FA CUP: "))
copaDaLigaInglesa = int(input("Títulos da Copa da Liga Inglesa: "))
superCopaDaInglaterra = int(input("Títulos da Super Copa da Inglaterra: "))
laliga = int(input("Títulos de Laliga: "))
copaDoRei = int(input("Títulos de Copa do Rei: "))
superCopaDaEspanha = int(input("Títulos de Super Copa da Espanha: "))
serieA = int(input("Títulos de serie A: "))
copaDaItalia = int(input("Títulos da Copa da Itália: "))
superCopaDaItalia = int(input("Títulos da Super Copa da Itália: "))
championsLeague = int(input("Títulos de Champions League: "))
superCopaDaUefa = int(input("Títulos de Super Copa da UEFA: "))
mundial = int(input("Títulos de Mundial de Clubes: "))
eurocopa = int(input("Títulos de Euro Copa: "))
nationsLeague = int(input("Títulos de Nations League: "))

coefSuperCopaDePortugal = superCopaDePortugal*1
coefPremierLeague = premierLeague*4
coefFaCup = faCup*3
coefCopaDaLigaInglesa = copaDaLigaInglesa*3
coefSuperCopaDaInglaterra = superCopaDaInglaterra*1
coefLaliga = laliga*3
coefCopaDoRei = copaDoRei*3
coefSuperCopaDaEspanha = superCopaDaEspanha*1
coefSerieA = serieA*2
coefCopaDaItalia = copaDaItalia*2
coefSuperCopaDaItalia = superCopaDaItalia*1
coefChampionsLeague = championsLeague*5
coefSuperCopadaUefa = superCopaDaUefa*1
coefMundial = mundial*2
coefEurocopa = eurocopa*4
coefNationsLeague = nationsLeague*3

resultado = (coefSuperCopaDePortugal + coefPremierLeague + coefFaCup + coefCopaDaLigaInglesa + coefSuperCopaDaInglaterra + coefLaliga + coefCopaDoRei + coefSuperCopaDaEspanha + coefSerieA + coefCopaDaItalia + coefSuperCopaDaItalia + coefChampionsLeague + coefSuperCopadaUefa + coefMundial + coefEurocopa + coefNationsLeague)

if (superCopaDePortugal + premierLeague + faCup + copaDaLigaInglesa + superCopaDaInglaterra + laliga + copaDoRei + superCopaDaEspanha + serieA + copaDaItalia + superCopaDaItalia + championsLeague + superCopaDaUefa + mundial + eurocopa + nationsLeague) != titulos :
    print("Quantidade de títulos errada!")
else:
    print("O coeficiente de títulos do Cristiano Ronaldo é: ",resultado)
