# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.
# Faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
# quanto pagou ao sindicato e o salário líquido.
# Observe que Salário Bruto - Descontos = Salário Líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo: (na lista)

salarioHora = float(input('Digite o quanto ganha por hora: '))
horasTrabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))
salarioBruto = salarioHora * horasTrabalhadas

valorIR = salarioBruto * (8/100)
valorINSS = salarioBruto * (11/100)
valorSindicato = salarioBruto * (5/100)
totalDescontos = valorIR + valorINSS + valorSindicato

salarioLiquido = salarioBruto - totalDescontos

print(f'\nFoi pago o total de {totalDescontos:.2f} Reais em desconto sendo eles: \n'
      f'INSS: {valorINSS:.2f} Reais \n'
      f'Imposto de Renda: {valorIR:.2f} Reais \n'
      f'Sindicato: {valorSindicato:.2f} Reais')
print(f'Seu salario bruto de: {salarioBruto:.2f} Reais'
      f'\nSe tornou um salario liquido de: {salarioLiquido:.2f} Reais')
