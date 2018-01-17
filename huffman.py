import string
import sys


RIGHT = 1
LEFT = 0

class Node:
	
	def __init__(self, child1, child2, letter):
		if child1!= None and child2!= None:
			self._children = []
			self._children.append(child1)
			self._children.append(child2)
		else:
			self._children = None
		
		self._letter = letter
		
		print "creating node for letter " + letter + " which has children ? " + str(self.hasChildren())
	
	def hasChildren(self):
		return self._children != None
		
		
def encode(alphabet_length, word):
	
	size = 0
	dict ={}
	for letter in xrange(alphabet_length):
		dict[string.ascii_uppercase[letter]] = 0
		size+=1
	
	for letter in word:
		dict[letter] += 1
	

	dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)
	
	t = dict.pop()
	while t[1] == 0:
		t = dict.pop()
	dict.append(t)
	
	
	pile = []
	while len(dict)!=0:
		t=dict.pop()
		node = Node(None, None, t[0])
		pile.insert(0, (node, t[1]))
		print "value = " + str(t[1])
	print
	
	n = 0
	while len(pile)>1:
		node1, value1 = pile.pop()
		node2, value2 = pile.pop()
		node3 = Node(node1, node2, str(n) )
		n +=1
		print "with children " + node1._letter + " and " + node2._letter + " of combined value " + str(value1 + value2) 
		print
		pile.append((node3, value1 + value2))
		pile = sorted(pile, key = lambda x: x[1], reverse = True)
	
	tree, tot = pile.pop()
	
	def recursivePrint(node):
		if node.hasChildren():
			recursivePrint(node._children[0])
			print node._letter,
			recursivePrint(node._children[1])
		else:
			print node._letter,
	
	recursivePrint(tree)
		
		
		
	
	
	
	code = []
	return code

def decode(alphabet_length, code):
	word = ""
	return word 


encode(26, "ILOVEROCKNROLL")
	
#print("code :"),
#for t in code :
#	print(t),
#print

#print("dict :")
#for t in sorted(dict) :
#	print t + " : " + str(dict[t]) + ", ",
#print

#print("word : " + word )