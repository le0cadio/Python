# faça um algoritmo que leia o preço do seu produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Digite o valor do seu produto: '))
valor = produto - (produto * 5 / 100)
print(f'o valor do seu produto com desconto é de {valor:.2f}')