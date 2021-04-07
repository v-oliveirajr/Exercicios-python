import math

# A pessoa entra com o valor da distância percorrida em km do diâmetro em cm
dist = int(input())
d = int(input())

# Arredondamento de pi pra 3 casas decimais
pi = round(math.pi, 3)

# Cálculo do comprimento da roda em Km
# Função pow faz o cálculo da potência
comprimento = pi * d * pow(10, -5)

# Cálculo do número de voltas: razão entre distância percorrida e comprimento da roda
num_vol = dist / comprimento

# A ordem de grandeza é a potência de 10 mais próxima desse número. Isso é a definição do logaritmo desse número na base
# 10. Usando a função round no print arredondamos o valor do logaritmo, obtendo assim a resposta da questão.
ordem = math.log10(num_vol)

# Observar que para printar as variáveis junto a textos transformarmos elas em strings antes usando str(), se não fizés-
# semos essa transformação daria erro

print('Distância percorrida: ' + str(dist) + 'km')
print('Diâmetro da roda:' + str(d) + 'cm')
print('Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a ' + str(round(ordem)))

