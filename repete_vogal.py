"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas
vogais duplicadas. 

Exemplo:
"Digite uma palavra:" Python
Saída: Pythoon

"""
import sys

def validar_string(s):
    if not s.isalpha():  # método usado para verificar se uma string contém apenas letras, retornando True ou False
        print("A string contém caracteres que não são letras, programa encerrado!")
        sys.exit(0) # encerra o programa imediatamente, sem executar as próximas linhas de código
    else:
        print("Sucesso: palavra contém apenas caracteres")

palavra = input(str("Digite uma palavra: \n"))
validar_string(palavra) # chama a função

resultado = ''
vogais = ["a","e","i","o","u"]
for letra in palavra:
    if letra in vogais:
        resultado += letra * 2 # se a letra for uma vogais, multiplica ela por 2
    else:
        resultado = resultado + letra # se a letra não for uma vogal, adiciona a mesma na variável resultado
print(resultado)
        