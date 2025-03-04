import sys 

"""
Na versão 1 desse arquivo tratamos erros com if/else, ou seja, verificamos se o arquivo existe antes de tentar
abri-lo. Nessa versão 2, vamos tratar erros com EAFP, ou seja, tentar abrir o arquivo e caso ocorra um erro,
tratamos esse erro com um bloco try/except.

Resumindo, temos a opção de verificar se alguma coisa pode dar errado antes de tentar fazê-la, ou tentar fazer algo
e tratar o erro caso ocorra (trato antes ou trato depois)
"""
# Tratando erros com EAFP
# EAFP - Easy to ask forgiveness than permissions
# É mais fácil pedir perdão do que permissão

try:
    names = open("names.txt").readlines()
    1 / 1
    print(names.append) 
except FileNotFoundError:
    print("[Error] file not found")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] you can't divide by zero")
    sys.exit(1)
except AttributeError:
    print("[Error] attribute not found")
    sys.exit(1)
else:
    print("Atributo existe")

try:  
    print(names[2])
except (IndexError, NameError) as e:
    print(f"[Error] {str(e)}")
    sys.exit(1)


