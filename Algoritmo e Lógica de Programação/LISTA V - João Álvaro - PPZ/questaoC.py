incremento = 0

for i in range(1067, 3627):
    if i % 2 == 0 and i % 7 == 0:
        incremento += 1
print(f'Existem {incremento} números que são pares e divisiveis por 7 entre 1067 e 3627')