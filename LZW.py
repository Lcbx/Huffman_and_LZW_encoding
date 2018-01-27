import string
from bitstring import BitArray, BitStream

# the number of bits used to encode a given sequence of characters
# an optimisation would be to make it dynamic : start small and add bits as the number of entries grow
BITS_USED = 12

def encode(word):
	
	# we build a dictionnary with all possible symbols and associate each of them with a number
	symbols ={}
	for letter in string.printable:
		bits = BitArray(BITS_USED)
		bits.uint = len(symbols)
		symbols[letter] = bits
	
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
			if len(symbols) < pow(2, BITS_USED):
				bits = BitArray(BITS_USED)
				bits.uint = len(symbols)
				symbols[temp] = bits
			
			# the sequence is reset to only the new character
			sequence = c
	
	# there is usually a last unincoded sequence to be added
	code.append(symbols[sequence])
	
	
	return code

def decode(code):
	
	# the string we'll  return
	word = ""

	# a list of all possible characters
	# (we dont need a dictionnary because we use integer offsets as encoding)
	symbols = []
	for letter in string.printable:
		symbols.append(letter)
	
	# the previous sequence
	previous = None
	
	# while there are still bits to read
	readBits = 0
	while readBits < len(code):
		
		readBits += BITS_USED
		
		# we read the current number in code
		i = code.read("uint:" + str(BITS_USED))
		
		# if it is within the known sequences
		if i < len(symbols)-1 :
			
			# we add its corresponding sequence from our list
			word += symbols[i]
			
			# if there was a previous sequence
			if len(symbols) < pow(2, BITS_USED) and previous != None :
				# we build a new sequence and add it to our known ones
				# by concatenation  of the previous sequence and the first character of the current one
				symbols.append(symbols[previous] + symbols[i][0])
		
		else:
			# special case : if during encoding the new sequence is used as soon as discovered,
			# it is used before eing even in the decoding dictionnary. No worries though, just use the concatenation of first char to previous sequence
			temp = symbols[previous] + symbols[previous][0]
			word += temp
			symbols.append(temp)
			
			
		# we reset our considered sequence to be c
		previous = i		
	
	# NOTE : keep in mind that we are decompressing, so we are not iterating character by character like in encode(), but sequence by sequence
	
	return word






