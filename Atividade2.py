""" Lista de compras 
    1 - Peça ao usuário que informe quantos itens deseja adicionar a lista
    2 - quantos itens o usuário ira levar 
    3 - e colocar em ordem alfabética
"""

Listas = []

print("\n*****  Lista de Compras  *****")
for i in range(4):
    
    produto = input("Digite o nome do produto que deseja adicionar: ")
    quantidade = int(input("Digite a quantidade do produto: "))

    Listas.append([produto, quantidade])

    if (i < 3):
        print("***Proximo produto***")

Listas.sort()

for Lista in Listas:
    print("\n****  LISTA DE COMPRA  *****")
    print(f"Produto : {Lista[0]} | Quantidade : {Lista[1]}")