# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite uma nota: '))
while nota > 10 or nota < 0:
    print('Digite apenas notas entre 0 a 10')
    nota = float(input('Digite uma nota novamente: '))
