# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores. Imprima os três vetores.
from random import randint
lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    j = randint(1, 100)
    lista1.append(j)
    lista3.append(j)
    j = randint(1, 100)
    lista2.append(j)
    lista3.append(j)

print(f'Lista 1: {sorted(lista1)} \nLista 2: {sorted(lista2)} \nLista 3: {sorted(lista3)}')