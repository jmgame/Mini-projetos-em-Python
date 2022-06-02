titulos = int(input("Informe a quantidade de títulos que o Messi tem: "))
print("\n")
laliga = int(input("Títulos de Laliga: "))
copaDoRei = int(input("Títulos de Copa do Rei: "))
superCopaDaEspanha = int(input("Títulos de Super Copa da Espanha: "))
ligueOne = int(input("Títulos de Ligue One: "))
championsLeague = int(input("Títulos de Champions League: "))
superCopaDaUefa = int(input("Títulos de Super Copa da UEFA: "))
mundial = int(input("Títulos de Mundial de Clubes: "))
copaAmerica = int(input("Títulos de Copa América: "))

coefLaliga = laliga*3
coefCopaDoRei = copaDoRei*3
coefSuperCopaDaEspanha = superCopaDaEspanha*1
coefLigueOne = ligueOne*2
coefChampionsLeague = championsLeague*5
coefSuperCopadaUefa = superCopaDaUefa*1
coefMundial = mundial*2
coefCopaAmerica = copaAmerica*3

resultado = (coefLaliga + coefCopaDoRei + coefSuperCopaDaEspanha + coefLigueOne + coefChampionsLeague + coefSuperCopadaUefa + coefMundial + coefCopaAmerica)

if (laliga + copaDoRei + superCopaDaEspanha + ligueOne + championsLeague + superCopaDaUefa + mundial + copaAmerica) != titulos :
    print("Quantidade de títulos errada!")
else :
    print("O coeficiente de títulos do Messi é: ",resultado)
