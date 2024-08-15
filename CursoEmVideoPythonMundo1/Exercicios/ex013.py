#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário: '))

ajuste = salario + (salario * 0.15)

print(f'Seu novo salário com ajuste de 15% é de: {ajuste} reais!')