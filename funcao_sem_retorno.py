import time


def recepcao():
  nome = input("Qual é o seu nome? ")
  print(f"Seja bem vindo, {nome} \n")


def questionarios():
  idade = input("Quantos anos voce tem? ")
  print(f"Legal, voce tem {idade} anos \n")
  moradia = input("E aonde voce mora? ")
  print(f"Que interessante, eu também moro em {moradia} \n")
  time.sleep(3)


def despedida():
  print("Foi muito bom conversar com você, até mais!")


recepcao()
questionarios()
despedida()
