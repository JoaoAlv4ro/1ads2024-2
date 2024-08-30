# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

username = str(input('Digite um nome de usuário: '))
password = str(input('Digite uma senha: '))
while username == password:
    print('Erro! Nome e senha de seu usuário não podem ser iguais.')
    username = str(input('Digite um nome de usuário: '))
    password = str(input('Digite uma senha: '))
