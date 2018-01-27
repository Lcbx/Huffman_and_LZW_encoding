import LZW
import huffman

import string
import random


def testEncodingDecoding(algorithm, word ):
	print "    " + algorithm.__name__
	code = algorithm.encode(word)
	print "\t code : \n" + str(code) + "\n" + str(len(code)/8) + "\n"
	result = algorithm.decode(code)
	print "\t result of decoding : \n" + result + "\n" + str(len(result)) + "\n"
	


random.seed(1286)
def generateRandomString(length = 0, alphabet_size = 0):
	
	if alphabet_size == 0 : alphabet_size = random.randint(2, len(string.printable))
	if length == 0 : length =  random.randint(10,10000)
	
	word = ""
	for c in xrange(length):
		word += string.printable[random.randint(0,alphabet_size-1)]
	return word



word = generateRandomString(500, 26)

print word + "\n" + str(len(word)) + "\n"
testEncodingDecoding(LZW, word)
testEncodingDecoding(huffman, word)
	
	
