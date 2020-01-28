import os

# Read File
def read_file(filename):
    products = []
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if '商品,price' in line:
                continue
            name, price = line.strip().split(',')
            print([name, price])
            products.append([name, price])
    return products


# Print Products
def print_products(products):
	for product in products:
		print(product)




# User input
def input_product(products):
	while True:
		name = input("input products Names:")
		if name == 'q':
			break
		price = input("Input the price:")
		# p = []
		# p.append(name)
		# p.append(price)
		products.append([name, price])
	return products

 
# Write File
def write_file(products,filename):
    with open(filename,'w', encoding='utf-8') as f:
        f.write('商品,price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + "\n")

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! ')
		products = read_file(filename)
	#print(products)
	else:
		print('File not found!!!')
	products = input_product(products)
	print_products(products)
	write_file(products,filename)

main()