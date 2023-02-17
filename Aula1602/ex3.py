valor = int(input("Digite um valor inteiro: "))
# 100, 50, 20, 10, 5, 2 , 1
cedulas = [0, 0, 0, 0, 0, 0, 0]
while True:
  if valor >= 100:
    cedulas[0] += int(valor / 100)
    valor = valor - (100 * cedulas[0])
  if valor >= 50:
    cedulas[1] += int(valor / 50)
    valor = valor - (50 * cedulas[1])
  if valor >= 20:
    cedulas[2] += int(valor / 20)
    valor = valor - (20 * cedulas[2])
  if valor >= 10:
    cedulas[3] += int(valor / 10)
    valor = valor - (10 * cedulas[3])
  if valor >= 5:
    cedulas[4] += int(valor / 5)
    valor = valor - (5 * cedulas[4])
  if valor >= 2:
    cedulas[5] += int(valor / 2)
    valor = valor - (2 * cedulas[5])
  if valor >= 1:
    cedulas[6] += valor

  break
print(
  "Cédulas de 100: {0}\nCédulas de 50: {1}\nCédulas de 20: {2}\nCédulas de 10: {3}\nCédulas de 5: {4}\nCédulas de 2: {5}\nMoedas de 1: {6}"
  .format(cedulas[0], cedulas[1], cedulas[2], cedulas[3], cedulas[4],
          cedulas[5], cedulas[6]))
