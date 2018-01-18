import string
from bitstring import BitArray, BitStream


# within the binary tree : 0 means left child, 1 means right child
RIGHT = '0b1'
LEFT = '0b0'

		
def encode(alphabet_length, word):
	
	# constructs the initial dictionnary with all possible simbols
	size = 0
	symbols ={}
	for letter in xrange(alphabet_length):
		symbols[string.ascii_uppercase[letter]] = 0
		size+=1
	
	# counts the number of occurences each symbol
	for letter in word:
		symbols[letter] += 1
	
#print(dict)
	
	# sort symbols by number of occurences
	symbols = sorted(symbols.items(), key = lambda x: x[1], reverse = True)
	
	# get rid of symbols that don't appear
	t = symbols.pop()
	while t[1] == 0:
		t = symbols.pop()
	symbols.append(t)
	
	
	## here we construct the binary tree with tuples :
	
	pile = symbols
	# while we don't have a lone root node
	while len(pile)>1:
		
		# get the two nodes with the least total occurences
		node1, value1 = pile.pop()
		node2, value2 = pile.pop()
		
		# the generated parent node
		node3 = (node1, node2)
		
		# we add it to the pile with its associated total value
		pile.append((node3, value1 + value2))
		
		# note : the leaves are the symbols themselves while intermediary nodes are tuples
		
		# sort them so we get the two nodes with the least total occurences next iteration
		pile = sorted(pile, key = lambda x: x[1], reverse = True)
	
	
	# the root node, we discard the occurence count now
	tree, tot = pile.pop()

#print tree
	
	
	# the code we'll return
	code = ""
	
	
	# we have to return the tree too for decoding later
	# here we don't bother much and add its string representation which is good enough
	code += (str(tree) + "#")
	
	
	## a recursive traversal of the tree allows us to create a dictionnary of matching symbols and codes for encoding :
	
	symbols = {}
	def buildCodeDict(symbols, node, code):
		# if its a leaf node, we add it and its representation to the dictionnary
		if type(node) is str:
			temp1 = BitArray(code)
			symbols[node] = temp1
		else:
			
			# else it's a parent node
			# we build the code corresponding to it's left and right child
			temp1 = BitArray(code)
			temp1.append(LEFT)
			buildCodeDict(symbols, node[0], temp1)
			
			temp2 = BitArray(code)
			temp2.append(RIGHT)
			buildCodeDict(symbols, node[1], temp2)
	
	# we called the defined function
	buildCodeDict(symbols, tree, BitArray())
	
	
	# finally we encode the word
	codedWord = BitArray()
	for letter in word :
		temp = symbols[letter]
		codedWord.append(temp)
		#print  letter + " : " + str(temp) + "\t  " + str(codedWord)
	
	code += codedWord.tobytes()
	
	return code

	
	
	
	
	
def decode(alphabet_length, code):
	
	
#print code
	
	# at the beginning of the code is a represetation of the encoding tree
	# we find it thanks to the "#" character that ends it
	tree = ""
	c = ""
	i = 0
	while c != "#":
		c = code[i]
		tree += c
		i += 1
	
	# a simple evaluation builds it
	tree = eval(tree)
	
#print tree
	
	# to avoid trying to interpret the tree
	code = code[i:] 
	
#print code
	
	
	# we cast the remain string as bits
	bitCode = BitStream(bytes = code ) #"0x" + code)
	bitCode = bitCode.read("bits:" + str(len(code)*8))
	
#print bitCode
	
	
	# all that's left is to interpret the bits with the tree
	word = ""
	node = tree
	# for each bit
	for t in bitCode :
		 # we iterate through the corresponding child node
		 node = node[t]
		 # if its a leaf node
		 if type(node) is str:
			 # we find the corresponding char
			 temp = node
			 # reset our place in the interpreting tree
			 node = tree
			 # add the char to the final word
			 word += temp
	
#print word	
	
	return word 


hello = encode(26, "ILOVEROCKNROLLPUTANOTHERDIMEINTHE")
print decode(26, hello)

	
#print("code :"),
#for t in code :
#	print(t),
#print

#print("dict :")
#for t in sorted(dict) :
#	print t + " : " + str(dict[t]) + ", ",
#print

#print("word : " + word )