import LZW
import huffman

import string
import random

import samples

def testEncodingDecoding(algorithm, sample ):
	print algorithm.__name__ + " : " + str( algorithm.decode(algorithm.encode(sample)) == sample )
	
def benchmark(algorithm, sample):
	print "compression ratio : " + str(len(sample)*8) + " / "+ str(len(algorithm.encode(sample))) + " (algorithm : " + algorithm.__name__ +")"

random.seed(1286)
def generateRandomString(length = 0, alphabet_size = 0):
	
	if alphabet_size == 0 : alphabet_size = random.randint(2, len(string.printable))
	if length == 0 : length =  random.randint(10,10000)
	
	word = ""
	for c in xrange(length):
		word += string.printable[random.randint(0,alphabet_size-1)]
	return word


algorithms = [LZW, huffman]




print "FAITHFULL ?"
for algorithm in algorithms:
		testEncodingDecoding(algorithm, samples.small)
print


print "WRITTEN TEXT"
for sample in samples.list :
	for algorithm in algorithms:
		benchmark(algorithm, sample)
print

		
print "RANDOM"
for j in range(3):
	if j == 0 :
		alphabet_size = 3
		print "\t small alphabet"
	if j == 1 :
		alphabet_size = 40
		print "\t medium alphabet"
	if j == 2 :
		alphabet_size = 98
		print "\t large alphabet"
	for i in range(4):
		length= pow(20, i+1)
		sample = generateRandomString(length, alphabet_size)
		for algorithm in algorithms:
			benchmark(algorithm, sample)
