
products = []
with open('products.csv','r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')
		print([name, price])
		products.append([name, price])

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

with open('products.csv','w', encoding='utf-8') as f:
	#f.write('商品,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + "\n")