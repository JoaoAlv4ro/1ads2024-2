# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

kmRodados = float(input('Quantos km foram percorridos? '))
diasAlugados = int(input('Por quantos dias o carro foi alugado? '))

valorDias = diasAlugados * 60
valorKm = kmRodados * 0.15

precoTotal = valorKm + valorDias

reais = int(precoTotal)
centavos = int((precoTotal - reais) * 100)

if diasAlugados == 0:
    mensagem = "Você não alugou o carro!"
elif diasAlugados > 0 and centavos > 0:
    mensagem = f'O preço total a se pagar pelo aluguel do carro é de: {reais} reais e {centavos} centavos'
else:
    mensagem = f'O preço total a se pagar pelo aluguel do carro é de: {precoTotal:.0f} reais'

print(mensagem)
