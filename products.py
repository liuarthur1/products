
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

for pp in products:
	print(pp[0], 'price is:', pp[1])