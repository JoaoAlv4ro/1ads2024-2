incremento = 0
for i in range(18644, 33087):
    if '2' in str(i) and '7' not in str(i):
        incremento += 1
print(f'Existem {incremento} números sortudos entre 18644 e 33087, segunda a Daniela')