listinha = []
soma = 0;

for i in range(0, 5):
    x = int(input("Adicione um valor na lista: "))
    listinha.insert(i, x)
    soma += x

print("A soma dos números é: {}".format(soma))
