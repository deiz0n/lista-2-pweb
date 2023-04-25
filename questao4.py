x = int(input("Digite um número: "))

if x > 0:
    print("O número {} é positivo.".format(x))
elif x < 0:
    print("O número {} é negativo.".format(x))
else:
    print("O número {} é neutro.".format(x))