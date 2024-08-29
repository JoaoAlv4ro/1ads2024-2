# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salarioAtual = float(input('Digite o salário atual: '))
porcentagemAumento = int(input('Digite a porcentagem do aumento: '))

aumento = salarioAtual * (porcentagemAumento/100)
novoSalario = salarioAtual + aumento

print(f'O novo salário será de: {novoSalario:.2f}')
print(f'Obteve-se um aumento de {aumento:.2f}!!')
