# A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

num = int(input('Digite um número inteiro: '))
numA = 1
numB = 1
i = 1

while i <= num-2:
    numA, numB = numB, numB + numB
    i += 1

print(numB)
