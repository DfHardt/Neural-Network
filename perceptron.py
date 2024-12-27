#Um perceptron é a menor unidade de uma rede neural, é uma estrutura análoga a um neurônio
#Implementação de um perceptron para dizer se um número é par ou ímpar

def main():
    x = int(input("Número:"))
    print(perceptron(x))


def dotProduct(input):
    weight = 1
    return input*weight

def activation(activationInput):
    if activationInput % 2 == 0:
        return 1
    return 0

def perceptron(input):
    output = activation(dotProduct(input))
    if output == 1:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    main()