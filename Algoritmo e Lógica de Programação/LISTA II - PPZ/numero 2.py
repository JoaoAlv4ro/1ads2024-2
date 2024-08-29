# Determine se um ano é bissexto.

ano = int(input('Digite um ano: '))
if (ano % 4) == 0:
    mensagem = f'{ano} é um ano bissexto'
else:
    mensagem = f'{ano} não é um ano bissexto'

print(mensagem)
