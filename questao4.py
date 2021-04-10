# Entrada de dados

def entrada():
    pontos = []
    x, y = input().split()
    x = int(x)
    y = int(y)
    pontos.append([x, y])
    while x or y != "":
        try:
            x, y = input().split()
            x = int(x)
            y = int(y)
            pontos.append([x, y])
        except ValueError:
            return pontos


pontos = entrada()
# Cálculo do centroide
def calculo():

    x = []
    y = []



    for val in pontos:
        for cont in range(2):
            if cont == 0:
                x.append(val[cont])
            if cont == 1:
                y.append(val[cont])

    centx = sum(x) / len(x)
    centy = sum(y) / len(y)

    Cent = (centx, centy)
    return Cent,centx,centy

Cent, centx, centy = calculo()
print("Centroide:", Cent)


import math

def comparacao(centx, centy):

    comparador1 = 0
    comparador2 = 100000000
    distmin = []
    distmax = []

    # Comparação das distâncias entre os pontos
    for val in pontos:
        for cont in range(len(val)):
            if cont == 0:
                diff1 = centx - val[cont]
            if cont == 1:
                diff2 = centy - val[cont]
                dist = math.sqrt(pow(diff1,2)+pow(diff2,2))
        if dist > comparador1:
            comparador1 = dist
            distmax = val
        if dist <= comparador1:
            if dist < comparador2:
                comparador2 = dist
                distmin = val

    return distmin, distmax


distmin, distmax = comparacao(centx,centy)

# Saída de dados

print("Ponto mais próximo do Centroide:", tuple(distmin))
print("Ponto mais distante do Centroide:", tuple(distmax))




