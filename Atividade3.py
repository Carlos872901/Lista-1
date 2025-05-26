"""  CAIXA ELETRONICO
    1 - Peça a valor a ser sacado
    2 - Se o valor for maior que o saldo disponivel, informe que n e possivel
    3 - Quando for ppssivel, calcule a quantidade de notas nessesarias para o saque
     3 - a) Com as notas de 100, 50, 20, 10, 5, 2
"""

saldo = 1000

valor = int(input("Digite o valor que deseja ser sacado: "))

if valor > saldo:
    print("O valor desejado e maior que seu saque. Informe outro valor.")

else:
    print(f"Saque de R$:{valor}. Aprovado retire suas notas:")

    notas = [100, 50, 20, 10, 5, 2]
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R${nota}")

        valor %= nota
    if valor !=0:
        print("Não foi possivel sacar todo o valor com as notas disponiveis no momento...")
