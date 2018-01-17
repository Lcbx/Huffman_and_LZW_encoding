import string
import sys


RIGHT = 1
LEFT = 0

		
def encode(alphabet_length, word):
	
	size = 0
	dict ={}
	for letter in xrange(alphabet_length):
		dict[string.ascii_uppercase[letter]] = 0
		size+=1
	
	for letter in word:
		dict[letter] += 1
	
	#print(dict)

	dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)
	
	t = dict.pop()
	while t[1] == 0:
		t = dict.pop()
	dict.append(t)
	
	

	while len(dict)>1:
		node1, value1 = dict.pop()
		node2, value2 = dict.pop()
		node3 = (node1, node2)
		dict.append((node3, value1 + value2))
		dict = sorted(dict, key = lambda x: x[1], reverse = True)
	
	tree, tot = dict.pop()
	
	Tree = tree

	print tree
		
	dict = {}
	def buildCodeDict(dict, node, code):
		if type(node) is str:
			temp1 = list(code)
			dict[node] = temp1
		else:
			temp1 = list(code)
			temp1.append(LEFT)
			buildCodeDict(dict, node[LEFT], temp1)
			temp2 = list(code)
			temp2.append(RIGHT)
			buildCodeDict(dict, node[RIGHT], temp2)
	
	buildCodeDict(dict, tree, [])
	
	#print(dict)
	
	
	code = []
	code.append(str(tree))
	for letter in word :
		temp = dict[letter]
		for t  in temp:
			code.append(t)
	
	return code

def decode(alphabet_length, code):
	
	word = ""
	
	tree = eval(code[0])
	node = tree
	for t in code[1:]:
		node = node[t]
		if type(node) is str:
			temp = node
			node = tree
			word += temp
			
	
	#print tree
	return word 


hello = encode(26, "ILOVEROCKNROLLPUTANOTHERDIMEINTHEJUKEBOXBABY")
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