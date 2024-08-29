# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

print('------- CONVERSOR - CELSIUS PARA FAHRENHEIT -------')
celsius = float(input('Digite quantos graus celsius: '))
fahrenheit = (9 * (celsius/5)) + 32

print(f'{celsius:.1f}°C seriam {fahrenheit:.1f}°F')
