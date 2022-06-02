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

