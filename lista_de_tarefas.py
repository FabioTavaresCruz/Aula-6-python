# 1 - Mostrar Todas as Tarefas
# 2 - Mostrar Tarefas Concluídas
# 3 - Mostrar Tarefas Pendentes
# 4 - Mostrar Tarefas por Prioridades
# 5 - Cadastrar Tarefas novas
# 6 - Finalizar Tarefa
# 7 - Remover Tarefa
# 0 - Sair

Tarefas = [
    {"Título":"Exercicios","Concluído":"SIM","Prioridade":"Alta"},
    {"Título":"Estudar","Concluído":"NÃO","Prioridade":"Alta"},
    {"Título":"Ler","Concluído":"SIM","Prioridade":"Baixa"},
    {"Título":"Arrumar a cama","Concluído":"NÃO","Prioridade":"Baixa"}
]

def todas():
  for lista in Tarefas:
    print (lista)

def concluidas():
  realizadas = "SIM"
  for lista in Tarefas:
    if (lista["Concluído"]) == realizadas:
      print(lista["Título"])

def pendentes():
   pendente = "NÃO"
   for lista in Tarefas:
      if (lista["Concluído"]) == pendente:
        print(lista)

def prioridades():
  prioridade = input ("Qual é a prioridade?: ")
  for lista in Tarefas:
    if lista["Prioridade"] == prioridade:
     print (lista["Título"])

def cadastrar():
    print ("---> Cadastrando uma nova tarefa <---")
    Titulo = (input("Adcione uma nova tarefa: "))
    Concluído = (input("Esta concluída?: "))
    Prioridade = (input("Qual é a prioridade?: "))

    nova_tarefa = {
      "Título":Titulo,
      "Concluído":Concluído,
      "Prioridade":Prioridade
    }
    Tarefas.append(nova_tarefa)

def finalizar():
  c = input("Qual tarefa deseja finalizar?: ")
  for tarefa in Tarefas:
    if tarefa["Título"] == c:
        tarefa["Concluído"] = "SIM"
        break
    
def remover():
  delete = (input("Remova a tarefa: "))

  for lista in Tarefas:
   if lista["Título"] == delete:
      Tarefas.remove (lista)
      break


while True: 

 print ("1 - Mostrar Todas as Tarefas")
 print ("2 - Mostrar Tarefas Concluídas")
 print ("3 - Mostrar Tarefas Pendentes")
 print ("4 - Mostrar Tarefas por Prioridades")
 print ("5 - Cadastrar Tarefas novas")
 print ("6 - Finalizar Tarefa")
 print ("7 - Remover Tarefa")
 print ("0 - Sair")

 opcao = input ("Escolhe uma opção: ")

 if opcao == "1":
   todas()

 elif opcao == "2":
   concluidas()

 elif opcao == "3":
   pendentes()

 elif opcao == "4":
   prioridades()

 elif opcao == "5":
   cadastrar()

 elif opcao == "6":
   finalizar()

 elif opcao == "7":
   remover()

 elif opcao == "0":
    print ("Saindo...")
    break
 
 else:
  print ("Opção inválida, tente novamente!!!")
 