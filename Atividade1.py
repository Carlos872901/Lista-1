"""Utilize o laço for para verificar os número primos de 1 a 100
   Ao final, mostre os números primos encontrados."""

print("\n=====Números primos de 1 a 100=====")

def primo (n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
primos = []

for numero in range(1, 101):
    if primo(numero):
        primos.append(numero)

print("\n===== Esses são os numeros primos encontrados de 1 a 100 =====")
print(primos)