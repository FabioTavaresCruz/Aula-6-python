notas = [7.0, 1.5, 10.0, 8.5, 3.0]


#contador = 0
#while contador <= 4:
#    print (f"A sua nota é: {notas[contador]}")
#    contador += 1
notas.append(float(input("Digite a nova nota: ")))

for x in notas:
    print (f"Sua nota é: {x}")
