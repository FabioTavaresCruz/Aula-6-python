# mostrar lista
# cadastrar item na lista
# excliur um item
# modificar item na lista
# saída

def mostrar():
  for x in lista:
    print (x)

def cadastrar():
  lista.append (input("Digite o novo item: "))
  print ("Item adcionado!")

def excluir():
  lista.remove (input ("Qual item deseja excluir: "))
  print ("Item removido!")

def modificar():
  item = input("Qual item deseja alterar?: ")
  item2 = lista.index (item)
  lista[item2] = input("Coloque o item: ")
  print ("Item alterado!")


lista = ["pão","leite","macarrão","manga","ovos"]

while True: 

 print ("1 - Mostrar lista")
 print ("2 - Cadastrar item na lista")
 print ("3 - Excluir item na lista")
 print ("4 - Modificar item na lista")
 print ("0 - Sair")

 opcao = input ("Escolhe uma opção: ")

 if opcao == "1":
   mostrar()

 elif opcao == "2":
   cadastrar()
 elif opcao == "3":
   excluir()
 elif opcao == "4":
   modificar()

 elif opcao == "0":
    print ("Saindo...")
    break
 
 else:
  print ("Opção inválida, tente novamente!!!")
 