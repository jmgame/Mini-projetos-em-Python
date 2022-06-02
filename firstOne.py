#c = float(input("escreva a temperatura em graus C: "))

#f = (c * 9/5) + 32

#print("a temperatura graus F: ", f)

#====================================================

#preco = float(input("Preço da gasolina: "))
#valor = float(input("valor a abastercer: "))

#l = float((valor/preco))

#print(f"você abasteceu {l:.2f} litros")

#===================================================

#nota1 = float(input("Escreva a sua primeira nota "))
#nota2 = float(input("Escreva a sua segunda nota "))

#media = float(nota1 + (nota2*2))/3

#passou = media >= 7

#print("sua média é de ", media)
#print("o aluno passou? ", passou)

#===================================================

#salario = float(input("Salário: "))
#reajuste = float(input("Reajuste: "))

#salReajust = salario + salario/100 * reajuste

#print("O salário reajustado é: ", salReajust)

#===================================================

#tipoCarteira = input("Qual sua categoria de carteira? ").upper()

#if tipoCarteira == "A" :
#    print("Você pode pilotar Motos e tricicolos!")

#elif tipoCarteira == "B" :
#    print("Você pode dirigir carros de passeio!")

#elif tipoCarteira == "AB" :
#    print("Você pode dirigir carros de passeio e pilotar motos e tricicolos!")

#elif tipoCarteira == "C" :
#    print("Você pode dirigir veículos acima de 3,5 toneladas!")

#elif tipoCarteira == "D" :
#    print("Você pode dirigir veículos com mais de 8 passageiros")

#elif tipoCarteira == "E" :
#    print("Você pode dirigir veículos com mais de 6 unidades acopladas (carretas).")

#else :
#    print("Informe uma categoria válida")

#===================================================

#import random

#ficar = True

#while ficar == True :

#    numDado = random.randint(1,6)
#    numTentativa = input("escreva o número soretado de 1 até 6: ")
    
#    if numTentativa == "sair" :
#        ficar = False 
#        continue

#   if int(numTentativa) == numDado : 
#      print("você acertou! ")

#    elif int(numTentativa) != numDado :
#       print("Você errou!")
    
#====================================================

#i = 0
#for i in range(101) :
#    if i % 2 != 0 : continue 
#    print(i)

#====================================================

#lista = ["abacate", "melão", "ameixa", "tangerina", "romã", "romã"]
#lista2 = []

#for repetir in lista :
#    if repetir not in lista2 :
#        lista2.append(repetir)
       
#print(lista2)

#====================================================

#lista1 = ["messi", "ronaldinho", "iniesta", "mascherano", "messi"]
#lista2 = ["messi", "xavi", "mascherano", "iniesta"]
#lista3 = []

#for abc in lista1 :
#    if abc in lista2 :
#        lista3.append(abc)
#print(len(lista3))
#print(lista3)

#====================================================

#palavraUsuario = input("Escreva a palvra: ")

#def pali(palavra) :

#   palind = palavra[::-1] 

#   if palind == palavra :
#        print("é pali")
#    else :
#        print("não é pali")

#pali(palavraUsuario)

#====================================================

'''from os import system, name

casas = [1,2,3,4,5,6,7,8,9]
fimJogo = False
#indica a vez no turo
vezJogadorA = True
vezJogadorB = False
#indica a casa escolhida
casaEscolhida = 0
#Quantidades de casas livres para finalizar o jogo
casasLivres = 9
#indicador casa
indicadorCasa = 'X'
#indicador ganhador
ganhador = "Velha"

def fazerTabuleiro() :
    
    for casa in range(9) :
        casa += 1
        

        print("[", "]", "\t", end="")
        if casa == 3 or casa == 6 :
            print("\n")

    print("\n")     
       
  

print("Jogador da vez", indicadorCasa)
    
fazerTabuleiro()

while not fimJogo:
    vaiJogar = int(input("Escolha uma casa válida ou digite 0 para sair: "))
    
    if vaiJogar == 0 :
        fimJogo == True

    if vaiJogar == 1:
        for casa in casas :
            casa += 1
            if casa == 2 :
                print("[ ", "x" " ]", "\t", end="")
            else : 
                print("[ ", " ]", "\t", end="")
            if casa == 4 or casa == 7 :
                print("\n") 
        vezJogadorB == True
        print("\n") 

    if vaiJogar == 2:
        for casa in casas :
                casa += 1
                if casa == 3 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 3:
        for casa in casas :
                casa += 1
                if casa == 4 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 4:
        for casa in casas :
                casa += 1
                if casa == 5 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 5:
        for casa in casas :
                casa += 1
                if casa == 6 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 6:
        for casa in casas :
                casa += 1
                if casa == 7 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 7:
        for casa in casas :
                casa += 1
                if casa == 8 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 8:
        for casa in casas :
                casa += 1
                if casa == 9 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n") 
        vezJogadorB == True
        print("\n") 
    if vaiJogar == 9:
        for casa in casas :
                casa += 1
                if casa == 10 :
                    print("[ ", "x" " ]", "\t", end="")
                else : 
                    print("[ ", " ]", "\t", end="")
                if casa == 4 or casa == 7 :
                    print("\n")

from os import system, name

casas = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
fimJogo = False
#indica a vez no turo
vezJogadorA = True
#indica a casa escolhida
casaEscolhida = 0
#Quantidades de casas livres para finalizar o jogo
casasLivres = 9
#indicador casa
indicadorCasa = 'X'
#indicador ganhador
ganhador = "Velha"

# Código acima errado, código abaixo interminado ----------------------------------------------------------------------------

def clear() :
    if name == 'nt' : _ = system('cls')
    else: _ = system('clear')


def fazerTabuleiro() :
    for casa in range(9):
        casa += 1
        print("[ ", casas[casa], " ]", "\t", end="")
        if casa == 3 or casa == 6 :    
            print("\n")
    print("\n")


def verificarGanhador() :
   return (casas[0] == casas[1]) and (casas[1] == casas[2]) or (casas[3] == casas[4]) and (casas[4] == casas[5]) or (casas[6] == casas[7]) and (casas[7] == casas[8]) or (casas[0] == casas[3]) and (casas[3] == casas[6]) or (casas[1] == casas[4]) and (casas[4] == casas[7]) or (casas[2] == casas[5]) and (casas[5] == casas[8]) or (casas[0] == casas[4]) and (casas[4] == casas[8]) or (casas[2] == casas[4]) and (casas[4] == casas[6])
        

while not fimJogo:
    clear()
    print("\n")
    print("Jogador da vez", indicadorCasa)
    print("\n")
    
    fazerTabuleiro()
    vaiJogar = int(input("Escolha uma casa válida para começar ou digite 0 para sair: "))


    if vaiJogar == "0" :
        fimJogo = True
    else :
        if vaiJogar <= 1 and vaiJogar <= 9:
            if ((not (int(casas[vaiJogar]) -1) == 'X') and (not (int(casas[vaiJogar]) -1) == 'O')) :
                casas[vaiJogar] = indicadorCasa
                vezJogadorA = not vezJogadorA
                casasLivres -= 1
                if(verificarGanhador()):
                    ganhador = "Jogador " + indicadorCasa
                    casasLivres = 0
                if casasLivres == 0 :
                    fimJogo == True
                if vezJogadorA == True :
                    indicadorCasa = "X"
                else :
                    indicadorCasa = "O"'''
