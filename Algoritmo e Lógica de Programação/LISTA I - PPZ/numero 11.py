# Sabendo que str() converte valores numéricos para string,
# calcule quantos dígitos há em 2 elevado a um milhão.
# CORREÇÃO: utilizar 10000 ao em vez de 1 milhão.

digitos = len(str(2**10000))
print(f'2 elevado a 10.000 possui {digitos} digitos')
