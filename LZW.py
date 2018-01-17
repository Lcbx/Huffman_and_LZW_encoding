import string


def encode(alphabet_length, word):
	size = 0
	dict ={}
	for letter in xrange(alphabet_length):
		dict[string.ascii_uppercase[letter]] = size
		size+=1

	code = []
	P = ""
	for c in word:
		temp = P+c
		if temp in dict:
			P = temp
		else:
			code.append(dict[P])
			dict[temp] = size
			size += 1
			P = c
	code.append(dict[P])
	
	return code #, dict

def decode(alphabet_length, code):
	word = ""

	size = 0
	dict = []
	for letter in xrange(alphabet_length):
		dict.append(string.ascii_uppercase[letter])
		size += 1

	P = None
	for c in code :
		word += dict[c]
		if P != None :
			dict.append(dict[P] + dict[c][0])
			size += 1
		P = c
	
	return word #, dict



	
#print("code :"),
#for t in code :
#	print(t),
#print

#print("dict :")
#for t in sorted(dict) :
#	print t + " : " + str(dict[t]) + ", ",
#print

#print("word : " + word )






