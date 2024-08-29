# Faça um Programa que leia três números e mostre o maior deles

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    mensagem = f'{num1} é o maior número'
elif num2 > num3:
    mensagem = f'{num2} é o maior número'
else:
    mensagem = f'{num3} é o maior número'

print(mensagem)
