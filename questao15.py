listinha = []

for i in range(0, 5):
    x = int(input("Adicione um valor na lista: "))
    listinha.insert(i, x)

numeroNaLista = int(input("Digite um valor que deseja buscar na lista: "))

for item in listinha:
    if item == numeroNaLista:
        print("O número {} está na lista.".format(numeroNaLista))
        break
    else: 
         print("O número {} não está na lista.".format(numeroNaLista))
         break