x = int(input("Digite um número: "))

def fibonacci(x):
    n1 = 0
    n2 = 1
    for i in range(0, x):
        print(n1, end=" ")
        n3 = n1 + n2
        n2 = n1
        n1 = n3

fibonacci(x)