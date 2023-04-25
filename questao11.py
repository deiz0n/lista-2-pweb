listinha = []

for i in range(0, 5):
    x = int(input("Adicione um valor na lista: "))
    listinha.insert(i, x)

print("Números ímpares da lista:")
for item in listinha:
    if item % 2 == 1:
        print(item, end=" ")