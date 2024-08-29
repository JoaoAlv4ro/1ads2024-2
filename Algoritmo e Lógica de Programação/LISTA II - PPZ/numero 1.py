#   Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
#   um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

def tipoTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'Equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'Isóceles'
    else:
        return 'Escaleno'

l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

if l1 > l2 + l3 or l2 > l1 + l2 or l3 > l1 + l2:
    mensagem = 'Invalido, os valores não forma um triangulo'
else:
    mensagem = f'O seu triângulo é: {tipoTriangulo(l1, l2, l3)}'

print(mensagem)
