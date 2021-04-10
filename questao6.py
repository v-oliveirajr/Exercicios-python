# Função que classifica a palavra como palíndromo, usando a variável comp

def pal(x):

    if len(x) <= 1:
        return
    else:
        comp = True
        for i in range(len(x)):
            if x[i] != x[len(x) - (i+1)]:
                comp = False
                return comp

        return comp


string = input()

# Se o usuário digitar o valor espaço ou apertar enter sem digitar nada o loop é encerrado
while string != "" and string != " ":
    comp = pal(string)
    if comp == True:
        print(string)
        string = input()
    else:
        string = input()

