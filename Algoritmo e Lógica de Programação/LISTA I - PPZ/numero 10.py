# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarrosDia = int(input('Quantos cigarros você fuma por dia? '))
anosFumando = int(input('A quantos anos você fuma? '))

totalDeFumo = cigarrosDia * anosFumando * 365
minutosPerdidos = totalDeFumo * 10

diasPerdidos = minutosPerdidos / 1440

print(f'Você perdeu por volta de {diasPerdidos:.0f} dias de vida por causa do cigarro!')