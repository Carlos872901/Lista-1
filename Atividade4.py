""" Cadastro de Usuario
    1- Peça o usuario seu nome e idade
    2- Pergunte ao final de cada cadastro se a pessoa deseja continuar
    3- O sistema deve rodar enquanto a resposta for s
    Ao final o programa deve mostrar
    1- Quantas pessoas foram cadastradas
    2- A media da idade
    3- O nome da pessoa mais velha"""

idade = 0
quantidade = 0
soma_idade = 0
mais_velho_nome = ""
mais_velho_idade = 0

while True:

    nome = input("\n Digite o seu nome: ")
    idade = int(input("\n Digite a sua idade: "))
    
    quantidade += 1
    soma_idade += idade

    if idade > mais_velho_idade:
        mais_velho_nome = nome
        mais_velho_idade = idade

    continuar = input("\n Deseja continuar? (S/N):").upper()
    if continuar != "S":
        break

media_idade = soma_idade / quantidade if quantidade  > 0 else 0
print("\n RESULTADO FINAL ")
print(f"\n Ao total foram cadastrados {quantidade} de pessoas.")
print(f"A media das idades foi de {media_idade} anos.")
print(f"O nome da pessoa mais velha e {mais_velho_nome} com {mais_velho_idade} anos. ")