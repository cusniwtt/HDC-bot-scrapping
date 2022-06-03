def check_slash(name):
	for i in range(len(name)):
		if name[i] == '/':
			first = name[:i]
			last = name[i+1:]
			name = first + ' or ' + last
	return name

text = 'ptinrekmkdfm/mksdkfjdfs.csv'
print(check_slash(text))