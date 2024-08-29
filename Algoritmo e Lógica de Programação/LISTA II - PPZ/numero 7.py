# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

metrosQuadrados = int(input('Digite quantos metros quadrados da parede que irá pintar: '))
if metrosQuadrados % 54 == 0:
    latasNecessarias = metrosQuadrados / 54
else:
    latasNecessarias = int(metrosQuadrados / 54) + 1

valorFinal = latasNecessarias * 80
print(f'Serão necessarias {latasNecessarias} latas')
print(f'O que será um total de: R$ {valorFinal:.2f}')
