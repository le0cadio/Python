# Aluguel de carros

diaria = int(input("Quantos dias você ficou com o carro? "))
km = float(input("Quantos km você rodou com o carro? "))

total = (diaria * 60) + (km * 0.15)

print(f'Você precisará pagar R$ {total: .2f} reais a locadora.')
