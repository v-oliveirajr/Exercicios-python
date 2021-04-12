# Vamos usar o formato de dicionário para armazenar os candidatos e seus respectivos números
ncand = int(input("Insira o número de candidatos"))
candidatos = {}
voto = 0
contbranco = 0
contnull = 0
votos = []
contagem_votos = {}


# Os votos válidos são colocados numa lista e então é feita uma contagem de cada um
for cont in range(ncand):
    nome, numero = input("Insira respectivamente o nome e o número dos candidatos, separados por #").split(sep='#')
    numero = int(numero)
    candidatos[numero] = nome
while voto >= 0:
    voto = int(input())
    if voto not in candidatos:
        if voto == 0:
            contbranco = contbranco+1
        else:
            contnull = contnull+1
    else:
        votos.append(voto)

candidatosv = list(candidatos.values())
candidatosn = list(candidatos.keys())

contagem_votos = candidatos

# A contagem é colocada num novo dicionário para então ser mostrada:

for element in set(votos):
    contagem_votos[element] = votos.count(element)

votos_totais = list(contagem_votos.values())


for i in range(len(candidatos)):
    print(candidatosv[i], candidatosn[i], "com "+str(votos_totais[i])+" voto(s).", sep=" - ")


print("Brancos", "com "+str(contbranco)+" voto(s).", sep=" - ")
print("Nulos", "com "+str(contnull)+" voto(s).", sep=" - ")