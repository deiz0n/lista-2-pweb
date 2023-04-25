listinha = []

for i in range(0, 5):
    x = int(input("Adicione um valor na lista: "))
    listinha.insert(i, x)

print("Ordem original da lista: {}".format(listinha))
listinha.sort()
print("Lista crescente: {}".format(listinha))