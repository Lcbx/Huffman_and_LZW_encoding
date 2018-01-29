import LZW
import huffman

import string
import random

import samples

	
def benchmark(algorithm, sample):
	originalBitSize = len(sample) *8
	encodedResult = algorithm.encode(sample)
	compressedSize = len(encodedResult)
	faithfull = algorithm.decode(encodedResult) == sample
	print "faithfull encryption : " + str(faithfull) +  " compression ratio : " + str(originalBitSize) + " / "+ str(compressedSize) + " = " + str(originalBitSize/float(compressedSize))+ " (" +algorithm.__name__ +")"

random.seed(1286)
def generateRandomString(length = 0, alphabet_size = 0):
	
	if alphabet_size == 0 : alphabet_size = random.randint(2, len(string.printable))
	if length == 0 : length =  random.randint(10,10000)
	
	word = ""
	for c in xrange(length):
		word += string.printable[random.randint(0,alphabet_size-1)]
	return word


algorithms = [LZW, huffman]



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
