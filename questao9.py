listinha = []
soma = 0

for i in range(0, 5):
    x = int(input("Adicione um valor na lista: "))
    listinha.insert(i, x)
    soma += x

media = soma / len(listinha)
print("Média da lista: {}".format(media))