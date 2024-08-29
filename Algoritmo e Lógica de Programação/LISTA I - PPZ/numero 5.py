# Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preco = float(input('Digite o preço do produto: '))
porcentagemDesconto = int(input('Digite a porcentagem do desconto: '))

desconto = preco * (porcentagemDesconto / 100)
precoComDesconto = preco - desconto

print(f'O novo preço será de: {precoComDesconto:.2f}')
print(f'Obteve-se um desconto de {desconto:.2f}!!')
