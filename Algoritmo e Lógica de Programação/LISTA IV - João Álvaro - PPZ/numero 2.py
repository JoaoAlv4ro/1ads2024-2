# Sorteie 20 inteiros entre 1 e 100 numa lista.
# Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.
from random import sample
lista = sample(range(100), 20)
par = []
impar = []

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Lista: {lista} \nNúmeros Pares: {par} \nNúmeros Impares: {impar}')

