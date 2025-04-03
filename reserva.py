"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponíveis para alugar e o preço de cada
quarto. Essa informação está disponível em um arquivo de texto separado por vírgulas. 

1,Suite Master,500
2,Quarto Família,400
3,Quarto casal,200
4,Quarto simples,100

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado e a quantidade de dias e no final
exibe o valor a ser pago. O programa deve salvar a escolha em outro arquivo contendo as reservas (reserva.txt). 
Se outro usuário tentar reservar o quarto, o programa deve exibir uma mensagem informando que o quarto já está
reservado. 

"""

with open("quartos.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

inf_quarto = input("Por favor, informe o código da acomodação\n") 
inf_dias = input("Quantos dias deseja ficar hospedado?\n")
inf_dias = int(inf_dias)

if inf_quarto == "1":
    with open("reserva.txt", "r") as file:
        conteudo = file.read()
        if inf_quarto in conteudo:
            print("Quarto já foi reservado, por favor, escolha outra opção")
        else:
            codigo_reserva = inf_quarto
            print(f"O custo da hospedagem será {inf_dias * 500}")
            with open("reserva.txt", "a", encoding="utf-8") as file:
                file.write(codigo_reserva)
                print("------------")

elif inf_quarto == "2":
    with open("reserva.txt", "r") as file:
        conteudo = file.read()
    if inf_quarto in conteudo:
            print("Quarto já foi reservado, por favor, escolha outra opção")
    else:
        codigo_reserva = inf_quarto
        print(f"O custo da hospedagem será {inf_dias * 400}")
        with open("reserva.txt", "a", encoding="utf-8") as file:
            file.write(codigo_reserva)
            print("------------")

elif inf_quarto == "3":
    with open("reserva.txt", "r") as file:
        conteudo = file.read()
    if inf_quarto in conteudo:
            print("Quarto já foi reservado, por favor, escolha outra opção")
    else:
        codigo_reserva = inf_quarto
        print(f"O custo da hospedagem será {inf_dias * 200}")
        with open("reserva.txt", "a", encoding="utf-8") as file:
            file.write(codigo_reserva)
            print("------------")

else:
    with open("reserva.txt", "r") as file:
        conteudo = file.read()
    if inf_quarto in conteudo:
            print("Quarto já foi reservado, por favor, escolha outra opção")
    else:
        codigo_reserva = inf_quarto
        print(f"O custo da hospedagem será {inf_dias * 100}")
        with open("reserva.txt", "a", encoding="utf-8") as file:
            file.write(codigo_reserva)
            print("------------")
