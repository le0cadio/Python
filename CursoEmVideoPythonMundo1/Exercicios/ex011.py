# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2

largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura * altura
tinta = area / 2
print(f'Com a area total de {area} necessita de {tinta} litros de tinta!')