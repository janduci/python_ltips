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
    raise RuntimeError("Ocorreu um erro") # Forçando um erro
except Exception as e: # Capturando o erro
    print(str(e)) # Exibindo a mensagem de erro

try:
    names = open("names.txt").readlines()
    1 / 1
    print(names.append) 
except FileNotFoundError: # Tratando erro de arquivo não encontrado
    print("[Error] file not found")
    sys.exit(1)
except ZeroDivisionError: # Tratando erro de divisão por zero
    print("[Error] you can't divide by zero")
    sys.exit(1)
except AttributeError: # Tratando erro de atributo não encontrado
    print("[Error] attribute not found")
    sys.exit(1)
else:
    print("Atributo existe")
finally:
    print("Execute isso sempre") # Sempre será executado, independente se houver erro ou não

try:  
    print(names[2])
except (IndexError, NameError) as e: # Tratando erro de índice não encontrado e erro de variável não definida
    print(f"[Error] {str(e)}")
    sys.exit(1)


