print("Bem vindo ao aplicativo para cálculo de IMC (Indice de Massa Corporal")


def calc_imc(peso, altura):
  imc = peso / (altura**2)
  return round(imc, 3)


peso = float(input("Digite o seu peso \n"))
altura = float(input("Digite a sua altura \n"))
imc = calc_imc(peso, altura)

print(f"O seu IMC é {imc}")

if imc < 18.5:
  print("Você está abaixo do peso \n")
elif imc < 24.9:
  print("Você está com peso normal \n")
else:
  print("Você está acima do peso \n")

print("Abaixo os valores de referência: \n")

valores = [
  "Abaixo de 18,5: baixo peso \n"
  "Entre 18,5 e 24,9: peso normal \n"
  "Entre 25 e 29,9: sobrepeso \n"
  "Igual ou superior a 30: obesidade \n"
]

for value in valores:
  print(value)