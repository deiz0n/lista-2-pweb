listinha = []

for i in range(0, 5):
    x = int(input("Adicione um valor na lista: "))
    listinha.insert(i, x)
    
print("Maior número: {} | Menor número: {}".format(max(listinha), min(listinha)))
        