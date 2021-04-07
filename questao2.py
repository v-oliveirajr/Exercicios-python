# Primeiramente fazemos um tratamento de erros para o caso do usuário não digitar um valor entre 1 e 50 para k

while True:
    try:
        k = int(input())
        if k < 1 or k > 50:
            raise ValueError
        break
    except ValueError:
        print("Digite apenas números de 1 a 50")


# Tratamento de erros para o caso do usuário digitar uma sequência maior que 50 caracteres
while True:
    try:
        s = input()
        if len(s) < 1 or len(s) > 50:
            raise ValueError
        break
    except ValueError:
        print("Digite uma sequência de motif de no máximo 50 caracteres")


# Tratamento de erros para o caso do usuário digitar uma sequência maior que 50 caracteres
while True:
    try:
        t = input()
        if len(t) < 1 or len(t) > 500:
            raise ValueError
        break
    except ValueError:
        print("Digite uma sequência de DNA de no máximo 500 caracteres")

# De acordo com o enunciado, percorremos todos os caracteres da string do DNA em busca de igualdades com a string motif
# Para isso usamos um loop for. Um dos pontos a se levar em conta é que python faz contagem dos índices a partir do 0,
# devemos sempre levar isso em consideração para não termos resultados inesperados.

# Dentro do loop determinamos t' (tl) como sendo um subconjunto dentro de t, cujo tamanho é o mesmo de s. Vamos determi-
# nar todos os subconjuntos possíveis dentro de t, começando por ACGGAT, o próximo é CGGATC e assim por diante.

for i in range(1, len(t) + 1 - len(s) + 1):

    tl = t[i-1:i+len(s)-1]
    tll = []
    cont = 0
# A partir da construção de t', vamos percorrer dentro dele os caracteres que sejam diferentes de s (usando um novo loop
# for) e para cada caractere diferente vamos contar +1 na nossa variável cont de contagem e inserir o índice correspon-
# dente numa lista usando a função append.
    for j in range(1, len(tl)+1):
        if tl[j-1] != s[j-1]:
            cont = cont+1
            tll.append(j)

# Depois de comparar os conjuntos t' e s, se o número de caracteres diferentes no total for menor que k (usando a variá-
# vel cont para determinar isso) aí sim nós iremos printar a posição dentro de t (variável i) e as posições dentro do
# subconjunto t' dadas pela lista tll.
    if cont <= k:
        print(i, tll)

# No final das contas o código vai obter todos os subconjuntos t' possíveis dentro de t que tenham o mesmo tamanho de s
# mas ele só mostrará os conjuntos que possuem no total k ou menos caracteres diferentes.





