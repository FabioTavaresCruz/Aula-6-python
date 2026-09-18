def circulo():
    raio = float(input("Diga o valor do raio: "))
    print ("O valor da área é", raio ** 2 * 3.14 ) 

def triangulo():
    base = float(input("Qual é o valor da base?: "))
    altura = float(input("Qual é o valor da altura?: "))
    print ("O valor da área é", base * altura / 2)

def quadrado():
    lado = float(input("Qual é o valor do lados?: "))
    print ("O valor da área é", lado ** 2)

def retangulo():
    base = float(input("Qual é o valor da base?: "))
    altura = float(input("Qual é o valor da altura?: "))
    print ("O valor da área é", base * altura)

def paralelograma():
    base = float(input("Qual é o valor da base?: "))
    altura = float(input("Qual é o valor da altura?: "))
    print ("O valor da área é", base * altura)

def losango():
    D = float(input("Diga o valor da diagonal maior: "))
    d = float(input("Diga o valor da diagonal menor: "))
    print ("O valor da área é", D * d / 2)

def trapezio():
    B = float(input("Diga o valor da base maior: "))   
    b = float(input("Diga o valor da base menor: "))   
    h = float(input("Diga o valor da altura: "))   
    print ("O valor da área é", B + b * h / 2)
    


while True: 
 print ("CALCULO DE FORMAS")
 print ("1 - Círculo")
 print ("2 - Triângulo")
 print ("3 - Quadrado")
 print ("4 - Retângulo")
 print ("5 - Paralelograma")
 print ("6 - Losango")
 print ("7 - Trapézio")
 print ("0 - Sair")

 opcao = input ("Escolhe uma opção: ")

 if opcao == "1":
  circulo()
 elif opcao == "2":
  triangulo()
 elif opcao == "3":
  quadrado()
 elif opcao == "4":
  retangulo()
 elif opcao == "5":
   paralelograma()
 elif opcao == "6":
   losango()
 elif opcao == "7":
   trapezio()


 elif opcao == "0":
  print ("Saindo...")
  break
 
 else:
  print ("Opção inválida, tente novamente!!!")