import sys

argumentos = sys.argv
qtde_argumentos = len(argumentos)

if qtde_argumentos < 3: 
    print("Por favor, informe pelo menos 2 números para realizar a operação.")
else: 
    numero1 = sys.argv[1]
    numero2 = sys.argv[2]
    qtde_argumentos = len(sys.argv)

    if numero1.isdigit() and numero2.isdigit():
        print("Os números informados são válidos.")

    if qtde_argumentos == 3:
        operacao = input("Informe a operação desejada (+, -, *, /): ")

        if operacao == "+":
            resultado = float(numero1) + float(numero2)
            print(f"O resultado da soma é: {resultado}")
        elif operacao == "-":
            resultado = float(numero1) - float(numero2)
            print(f"O resultado da subtração é: {resultado}")
        elif operacao == "*":
            resultado = float(numero1) * float(numero2)
            print(f"O resultado da multiplicação é: {resultado}")
        elif operacao == "/":
            resultado = float(numero1) / float(numero2)
            print(f"O resultado da divisão é: {resultado}")
    else:
        resultado = "Operação inválida"
