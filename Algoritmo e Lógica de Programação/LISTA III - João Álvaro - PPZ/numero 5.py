# Dados dois números inteiros positivos, determinar
# o máximo divisor comum entre eles usando o algoritmo de Euclides

numA = int(input('Digite o primeiro número: '))
numB = int(input('Digite o segundo número: '))

while numA % numB != 0:
    numA, numB = numB, numA % numB

print(f'O multiplo divisor comum é {numB}')
