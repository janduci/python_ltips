try:
    numero = int(input("Digite um número inteiro: "))  
    resultado = 100 / numero                         
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print(f"Divisão bem-sucedida! O resultado é {resultado}.")
