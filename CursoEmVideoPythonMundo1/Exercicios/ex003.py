#Desafio: Crie um programa que leia dois números e mostre a soma entre eles


numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
s = numero1 + numero2
#print('A soma entre:', n1, 'e', n2, 'é: ', s)
print('A soma entre {} e {} é {} '.format(numero1, numero2, s))
