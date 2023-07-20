#!/usr/bin/python3

pizzas = ['Cheese','Pepperoni','Veggie','Margherita','Hawaiian','Sicilian']

friend_pizzas = pizzas[:]

pizzas.append('Paneer')

friend_pizzas.append('BBQ')

print("My favourite pizzas are: ")
for pizza in pizzas:
	print(pizza)

print("My friends favourite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)
