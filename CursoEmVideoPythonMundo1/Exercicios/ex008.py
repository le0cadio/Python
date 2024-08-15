# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
valor = int(input('Digite um valor: '))

centimetro = valor * 100
milimetro = valor * 1000
decametro = valor / 10
hectometro = valor / 100
quilometro = valor / 100

print(f'seu valor convertido em centimetros é de: {centimetro} e convertido em milimetros é de: {milimetro} ')
print(f' seu valor convertido em decametro é de : {decametro} e convertido em hectometro é de:  {hectometro}')
print(f'seu valor convertido em quilometro é de : {quilometro}')
