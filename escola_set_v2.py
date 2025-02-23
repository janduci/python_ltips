# objetivo é listar os alunos por tipo de aula
# criando váriaveis do tipo lista para receber os alunos
sala1 = ["maria", "jose"]
sala2 = ["pedro", "rosa"]

# criando váriaveis do tipo lista para receber os alunos por tipo de aula
aula_futebol = ["jose", "pedro"]
aula_ballet = ["maria", "rosa"]

# organizando os tipos de aula em uma tupla dentro de uma lista e adicionando um label 
# para cada tipo de aula
atividades = [("futebol", aula_futebol), ("ballet", aula_ballet)]

# criando um loop para percorrer a lista de atividades e imprimir os alunos por tipo de aula
# e irei desacoplar a tupla em duas variáveis

for nome_atividade, atividade in atividades:
    print(f"Alunos da aula de {nome_atividade}:")
    atividade_sala1 = set(atividade).intersection(sala1)
    atividade_sala2 = set(atividade).intersection(sala2)
    print()
    print(f"Alunos da sala 1: {atividade_sala1}")
    print()
    print("-" * 40)
    print()
    print(f"Alunos da sala 2: {atividade_sala2}")
    print()
    print("#" * 40)
    print()