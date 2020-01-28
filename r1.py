
# Read File
def read_file(filename):
	lines = []
	with open(filename,'r', encoding='utf-8-sig') as f:
		for line in f:
			#data = f.read()
			lines.append(line.strip())
			#print(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == "Allen":
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ':' + line )
	#print(new)
	return(new)

def write_file(filename, Lines):
	with open(filename,'w',encoding='utf-8') as f:
		for line in Lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output1.txt', lines)

main()