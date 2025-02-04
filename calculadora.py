operacao = input("operacao [sum, sub, mult, div]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

def soma(a, b):
  return a + b

 
operacoes = {
  "sum": soma,
  "sub": lambda a, b: a - b,
  "mult": lambda a, b: a * b,
  "div": lambda a, b: a / b,
}

print(operacoes[operacao](int(n1), int(n2)))

"""
Comparando a denição/escrita de funções

def soma(a, b):
  return a + b

lambda a, b: a + b

No final são a mesma coisa, mas a primeira é mais explicita e a segunda é mais "limpa"
""" 