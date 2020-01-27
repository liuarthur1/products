
products = []
while True:
	name = input("input products Names:")
	if name == 'q':
		break
	price = input("Input the price:")
	# p = []
	# p.append(name)
	# p.append(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'price is:', p[1])