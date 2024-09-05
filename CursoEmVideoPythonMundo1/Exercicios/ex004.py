# Desafio: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as possíveis informações sobre ele.

a = input('Digite alguma coisa : ')
print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em letras maiúsculas?{a.isupper()}')
print(f'Está em letras minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')
print('O tipo primitivo desse valor é: ', type(a))