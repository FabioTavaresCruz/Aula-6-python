clientes = [
    {"nome":"Ana","cel":"11878","empresa":"FIAT"},
    {"nome":"Pedro","cel":"15332","empresa":"INTEL"},
    {"nome":"Maria","cel":"44444","empresa":"SEBRAE"},
    {"nome":"Felipe","cel":"55555","empresa":"INTEL"},
]

empresa_digitada = input ("Digite o nome da empresa: ")
for cliente in clientes:
    if cliente["empresa"] == empresa_digitada:
     print (cliente)


print ("---> Cadastrando um novo cliente <---")
nome = (input("Adcione um novo cliente: "))
cel = (input("Adcione um novo celular: "))
empresa = (input("Adcione a empresa do cliente: "))

novo_cliente = {
   "nome":nome,
   "cel":cel,
   "empresa":empresa
}
clientes.append(novo_cliente)
print (clientes)

print ("---> Excluindo um cliente pelo nome <---")
nome_del = (input("Delete cliente: "))

for cliente in clientes:
   if cliente["nome"] == nome_del:
      clientes.remove (cliente)
      break
print (clientes)