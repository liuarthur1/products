
lines = []
with open('3.txt','r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
		#print(line)

for line in lines:
	s = line.split(" ")
	person = s[0][5:]
	print(person)
	print(s)
