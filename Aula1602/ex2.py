# 0= nulo, 1= c1, 2=c2, 3=c3, 4=branco
votos = [0, 0, 0, 0, 0]
condicao = ["Nulos", "Candidato 1", "Candidato 2", "Candidato 3", "Brancos"]
print("Votação Anual de Representante de Sala")
for i in range(5):
  votos[i] = int(input("Votos {0}: ".format(condicao[i])))
total = sum(votos)
print(
  "Total de Votos: {0}\nNulos: {1} | {2}%\nCandidato 1: {3} | {4}%\nCandidato 2: {5} | {6}%\nCandidato 3: {7} | {8}%\nBrancos: {9} | {10}%"
  .format(total, votos[0], int(votos[0] * 100 / total), votos[1],
          int(votos[1] * 100 / total), votos[2], int(votos[2] * 100 / total),
          votos[3], int(votos[3] * 100 / total), votos[4],
          int(votos[4] * 100 / total)))

# total = 100
# candidato = x
