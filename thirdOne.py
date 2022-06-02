from posixpath import split

nomeArqv = "campeonato-brasileiro-full.csv"

arqv = open(nomeArqv, mode='r')

conteudo = arqv.read()

arqv.close

itens = conteudo.splitlines()

informe = input("Informe o nome do time que participou do Campeonato Brasileiro 2021: ")


def funcMostraPartida() :   
    
    pontos = 0
    pontosEmpate = 0
    for item in itens :
        
        item = item.split(',')

        if  informe == item[5] or informe == item[6]:
            print(item[5], " x ",item[6])

        if informe == item[11] :
            pontos += 3    

        elif  (informe == item[5] or informe == item[6]) and item[11] == '-' :
            pontosEmpate += 1

    print("\nO ", informe, "fez essa quantidade de pontos: ", pontos+pontosEmpate)

    """for i in item :
        
        print(f"{i}\t", end="")"""

funcMostraPartida()
    




        


