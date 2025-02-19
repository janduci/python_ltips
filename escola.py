sala1 = ["alex", "catarina", "isadora", "janduci"]
sala2 = ["abel", "maria", "joão", "pedro", "raquel"]

aula_ingles = ["alex", "abel", "catarina", "maria"]
aula_musica = ["janduci", "joão", "pedro", "raquel", "isadora"]

atividades = [
  ("Inglês", aula_ingles),
  ("Música", aula_musica),
]

for nome_atividade, atividade in atividades:

  print(f"Alunos da atividade {nome_atividade}: \n")
  print("-" * 40)
  
  atividade_sala1 = []
  atividade_sala2 = []

  for aluno in atividade:
    if aluno in sala1:
      atividade_sala1.append(aluno)
    elif aluno in sala2:
      atividade_sala2.append(aluno)

  print("Sala1 ", atividade_sala1)
  print("Sala2 ", atividade_sala2)
  print()
  print("#" * 40)


      
