print("Escreva 10 numeros inteiros")
maior = 0
menor = 0
v = 0
for i in range(10):
  v = int(input("Numero {0}: ".format(i + 1)))
  if i == 0:
    maior = v
    menor = v
  maior = max(maior, v)
  menor = min(menor, v)

print("Maior: {0}, Menor: {1}".format(maior, menor))