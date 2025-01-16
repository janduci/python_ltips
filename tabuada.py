__version__ = "0.0.1"
__author__ = "Janduci"
__license__ = "Unlicense"

numeros = list(range(1, 11)) 
print(numeros)

for numero in numeros:
    print(f"Tabuada do {numero}:")
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-----------------")
  
          
