# Primeiramente fazemos um tratamento de erros para o caso do usuário digitar algum valor nulo. Se o usuário digitar um
# número negativo o valor será invertido.

while True:
    try:
        l = int(input("Insira o número de lojas"))
        p = int(input("Insira o número de produtos pequisados"))
        if l < 0:
            l = -l
        if p < 0:
            p = -p
        if l == 0 or p == 0:
            raise ValueError
        break
    except ValueError:
        print("Erro: valor nulo digitado")

lo = []
po = []
mini = []
maxi = []



import random as rd

for i in range(1,l+1):
        lo.append(input("Nome da loja "+ str(i)))

for i in range(1,p+1):
        po.append(input("Nome do produto " + str(i)))
        mini.append(float(input("Valor mínimo do produto "+ str(i))))
        maxi.append(float(input("Valor máximo do produto "+ str(i))))

# Calcula os valores aleatórios dentro das faixas especificadas
v = []
for i in range(l):
    lojas = []
    for j in range(p):
        lojas.append(round(rd.uniform(mini[j],maxi[j]),ndigits = 2))
    v.append(lojas)


# Compara os valores e coloca os menores numa lista de índices a ser acessada pela tabela de lojas depois
index = [None]*p
menores = [None] *p

for col in range(len(po)):
    comparador = maxi[col]
    for li in range(len(v)):
        if v[li][col] <= comparador:
            index[col] = li
            menores[col] = v[li][col]
            comparador = v[li][col]


# Mostrar a tabela inserida pelo usuário
print('\n',''"Resultado da pesquisa:")

for cont in range(len(v)):
    if cont == 0:
        print('\t',*po,sep = '\t')
    print(lo[cont],*v[cont],sep = '\t')


# Mostra a tabela das lojas mais baratas, usando a lista de índices criada anteriormente
print('\n','Menores preços:')
for cont in range(p):
    print(po[cont],lo[index[cont]])

# Mostra o valor total fazendo a soma de uma lista criada com os menores valores para cada produto
print('\n',"Valor total:",'\n','R$ ',round(sum(menores),ndigits = 2))












