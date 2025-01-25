# formula de Heron

def heron(a, b, c):
  perimeter = a + b + c
  s = perimeter // 2
  area = s * (s - a) * (s - b) * (s - c)
  return area**0.5

formula = heron(5, 6, 7)
print(formula)

# reutilizando a fórmula acima

triangulos = [
    (3, 4, 5),
    (4, 7, 9),
    (5, 12, 13),
]

for t in triangulos:
  area = heron(t[0], t[1], t[2])
  print(f"A área do triângulo é: {area}")
