#  Faça agora o contrário, de Fahrenheit para Celsius.

print('------- CONVERSOR - FAHRENHEIT PARA CELSIUS -------')
fahrenheit = float(input('Digite quantos graus fahrenheit: '))
celsius = (fahrenheit - 32) * (5/9)

print(f'{fahrenheit:.1f}°F seriam {celsius:.1f}°C')
