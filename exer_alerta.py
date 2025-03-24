"""
Alarme de temperatura

Script que pergunta ao usuário qual a temperatura atual e o índice de umidade
do ar onde será exibida uma mensagem de alerta dependendo das condições.

Temperatura maior que 45: Alerta!!! Perigo, calor extremo.
Temperatura * 3 for maior ou igual a umidade: Alerta!!! Perigo de calor umido!  
Temperatura entre 10 e 30: Normal
Temperatura entre 0 e 10: Frio
Temperatura <0: Alerta!!! Frio extremo

Utilizar try exceptions para controlar a entrada do usuário

Validar se o que usuário digitou é um numero (isdigit()) e se não for, exibir mensagem 
de erro

Usuário digitou uma string ao invés de um número, exibir mensagem de erro
could not convert string to float

Usuário não digitou nada, exibir mensagem de erro
O mesmo erro acima, pois toda entrada padrão do python é uma string

Sim, toda entrada do usuário em Python obtida por meio da função input() é sempre do tipo 
str (string), independentemente do que for digitado.
"""

# faixa de medição da umidade é de 0 a 100%

temperatura = float(input("Qual é a temperatura atual? "))
umidade = float(input("Qual é o índice de umidade do ar? "))

try: 
    if temperatura > 45:
        print("Alerta!!! Perigo, calor extremo")

    elif temperatura * 3 >= umidade:
        print("Alerta!!! Perigo de calor umido ")

    elif temperatura > 10 < 30:
        print("Normal")
# dependendo do valor da temperatura e da umidade, vai dar match no primeiro elif

    elif temperatura > 0 < 10:
        print("Frio")

    elif temperatura < 0:
        print("Alerta!!! Frio extremo")

except ValueError:
    print("Could not convert string to float")

except Exception as error:
    print("Unknown error")

finally:
    print("End of the program")





 
