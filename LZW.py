import string
from bitstring import BitArray, BitStream

# the number of bits used to encode a given sequence of characters
# an optimisation would be to make it dynamic : start small and add bits as the number of entries grow
BITS_INDEX = 12

def encode(word):
	
	# we build a dictionnary with all possible symbols and associate each of them with a number
	size = 0
	symbols ={}
	for letter in string.printable:
		bits = BitArray(BITS_INDEX)
		bits.uint = size
		symbols[letter] = bits
		size+=1
	
	# the code we'll  return
	code = BitStream()
	
	# a sequence of characters
	sequence = ""
	
	# for each character in the word we are encoding
	for c in word:
		
		# we add it to the sequence we are currently considering
		temp = sequence + c
		
		# if we know the result we just keep it and parse the next character
		if temp in symbols:
			sequence = temp
			
		# otherwise
		else:
		
			# we add the previously known sequence to the code
			code.append(symbols[sequence])
			
			# and add the new sequence to our dictionnary of known sequences
			if len(symbols) < pow(2, BITS_INDEX):
				bits = BitArray(BITS_INDEX)
				bits.uint = size
				symbols[temp] = bits
				size += 1
			
			# the sequence is reset to only the new character
			sequence = c
	
	# there is usually a last unincoded sequence to be added
	code.append(symbols[sequence])
	
	
	return code

def decode(code):
	
	currentBitIndex = BITS_INDEX
	
	# the string we'll  return
	word = ""

	# a list of all possible characters
	# (we dont need a dictionnary cause we use integer offsets as encoding)
	symbols = []
	for letter in string.printable:
		symbols.append(letter)
	
	# the previous sequence
	sequence = None
	
	# while there are still bits to read
	for _ in xrange(len(code)/BITS_INDEX) :
		
		# we read the current number in code
		i = code.read("uint:" + str(BITS_INDEX))
		
		# we add its corresponding sequence from our list
		word += symbols[i]
		
		# if there was a previous sequence
		if len(symbols) < pow(2, BITS_INDEX) and sequence != None :
			# we build a new sequence and add it to our known ones
			# by concatenation  of the previous sequence and the first character of the current one
			symbols.append(symbols[sequence] + symbols[i][0])
		
		# we reset our considered sequence to be c
		sequence = i
	
	print "len(symbols) = " + str(len(symbols))
	
	# NOTE : keep in mind that we are decompressing, so we are not iterating character by character like in encode(), but sequence by sequence
	
	return word






