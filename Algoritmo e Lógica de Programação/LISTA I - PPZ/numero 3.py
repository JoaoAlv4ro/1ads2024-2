# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

dias = int(input('Digite quantos dias: '))
horas = int(input('Digite quantas horas: '))
minutos = int(input('Digite quantos minutos: '))
segundos = int(input('Digite quantos segundos: '))

dias *= 86400
horas *= 3600
minutos *= 60

segundosTotais = dias + horas + minutos + segundos

print(f'A quantia total de segundos é de: {segundosTotais}')
