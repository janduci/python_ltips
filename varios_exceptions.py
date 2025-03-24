try:
    numero = int(input("Digite um número:\n"))

    resultado = 10 / numero
    print(f"O resulto da divisao de 10 por {numero} é {resultado}")
# se um erro for levantado no bloco acima, o Python interrompe a execução do programa e
# vai direto para o bloco except correspondente ao erro levantado, ignorando o restante
# do código, caso contrário, ele executa o próximo bloco de código.

    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except ZeroDivisionError:
    print("Não é possível dividir por zero")

except ValueError:
    print("Você não digitou um número inteiro")

except FileNotFoundError:
    print("Arquivo não encontrado") 

except Exception as error:
    print("Erro desconhecido")

finally:
    print("Fim do programa")


                 