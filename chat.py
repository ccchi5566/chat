def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	new = []
	person = None #先預設參數為無 不然chat中第一行不是溫于森或詠麒的話會當掉
	for line in lines:
		if line == '溫于森':
			person = '溫于森'
			continue
		elif line == '詠麒':
			person = '詠麒'
			continue

		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
