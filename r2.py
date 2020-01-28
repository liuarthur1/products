
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
	allen_count = 0
	allen_img_count = 0
	viki_count = 0
	viki_img_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_img_count += 1
			else:
				for m in s[2:]:
					allen_count += len(m)
			#print(s[2:])
		elif name == 'Viki':
			if s[2] == '圖片':
				viki_img_count += 1
			else:
				for m in s[2:]:
					viki_count += len(m)

	print('Allen images:', allen_img_count)
	print('Viki images:', viki_img_count)				
	print('Allen Talks:', allen_count)
	print('Viki Talks:', viki_count)
			#print(s[2:])


	#print(new)
	return(new)


def write_file(filename, Lines):
	with open(filename,'w',encoding='utf-8') as f:
		for line in Lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output1.txt', lines)


main()