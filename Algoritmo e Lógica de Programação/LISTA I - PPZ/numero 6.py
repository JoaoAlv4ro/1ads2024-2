# Calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input('Digite a Distancia a ser percorrida: '))
velocidade = int(input('Digite a Velocidade Média esperada para a viagem: '))

tempo = distancia/velocidade

if tempo < 1:
    tempo *= 60
    minutagem = 'minutos'
else:
    minutagem = 'hora' if tempo == 1 else 'horas'

print(f'O tempo de viagem será de: {tempo:.0f} {minutagem}')
