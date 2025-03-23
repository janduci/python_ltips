# Faça um programa que imprime os números pares de 1 a 200

for numero in range(1,201):
    if numero % 2 == 0:
        print(numero)

# Versão do professor

for numero in range(1, 201):
    if numero % 2 != 0:
        continue
