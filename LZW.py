import string


def encode(word):
	size = 0
	symbols ={}
	for letter in string.printable:
		symbols[letter] = size
		size+=1

	code = []
	P = ""
	for c in word:
		temp = P+c
		if temp in symbols:
			P = temp
		else:
			code.append(symbols[P])
			symbols[temp] = size
			size += 1
			P = c
	code.append(symbols[P])
	
	return code #, symbols

def decode(code):
	word = ""

	size = 0
	symbols = []
	for letter in string.printable:
		symbols.append(letter)
		size += 1

	P = None
	for c in code :
		word += symbols[c]
		if P != None :
			symbols.append(symbols[P] + symbols[c][0])
			size += 1
		P = c
	
	return word #, symbols



	
#print("code :"),
#for t in code :
#	print(t),
#print

#print("symbols :")
#for t in sorted(symbols) :
#	print t + " : " + str(symbols[t]) + ", ",
#print

#print("word : " + word )






