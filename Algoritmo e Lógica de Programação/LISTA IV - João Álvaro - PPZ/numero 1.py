# Sorteie 10 inteiros entre 1 e 100 para uma lista
# e descubra o maior e o menor valor,
# sem usar as funções max e min.
from random import sample
lista = sample(range(100), 10)
max = min = lista[0]

for i in lista:
    if i > max:
        max = i
    elif i < min:
        min = i

print(f'Lista: {lista} \nMaior Número: {max} \nMenor Número: {min}')
