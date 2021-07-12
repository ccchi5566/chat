def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
		return lines


def convert(lines):
	person = None
	余俊霆_word_count = 0
	詠麒_word_count = 0
	余俊霆_sticker_count = 0
	詠麒_sticker_count = 0
	余俊霆_image_count = 0
	詠麒_image_count = 0	
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '余俊霆':
			if s[2] == '[貼圖]':
				余俊霆_sticker_count += 1
			elif s[2] == '[圖片]':
				余俊霆_image_count += 1
			else:
				for m in s[2:]:
					余俊霆_word_count += len(m)
		elif name == '詠麒':
			if s[2] == '[貼圖]':
				詠麒_sticker_count += 1 
			elif s[2] == '[圖片]':
				詠麒_image_count += 1
			else:
				for m in s[2:]:
					詠麒_word_count += len(m)
	print('俊霆說了', 余俊霆_word_count, '傳了', 余俊霆_sticker_count, '個貼圖', '傳了',余俊霆_image_count, '圖片' )
	print('詠麒說了', 詠麒_word_count, '傳了', 詠麒_sticker_count, '個貼圖', '傳了',詠麒_image_count, '圖片' )


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE] 與余俊霆的聊天.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()