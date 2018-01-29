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
			if len(symbols) < 1<<BITS_USED:
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
	
	# the first sequence (a lone symbol)
	previous = symbols[ code.read("uint:" + str(BITS_USED)) ]
	readBits = BITS_USED
	word += previous
	
	# NOTE : readBits is the number of bits we've read till now, would be usefull if we a dynamic value for BITS_USED
	
	# while there are still bits to read
	while readBits < len(code):
		
		# we read the current number in code
		i = code.read("uint:" + str(BITS_USED))
		readBits += BITS_USED
		
		# if it is within the known sequences
		if i < len(symbols) :

			# we add its corresponding sequence from our list
			sequence = symbols[i]
			word += sequence
			
			# if there was a previous sequence
			if len(symbols) < 1<<BITS_USED :
				# we build a new sequence and add it to our known ones
				# by concatenation  of the previous sequence and the first character of the current one
				symbols.append(previous + sequence[0])
				
		
		else:
			# special case : if during encoding the new sequence is used as soon as discovered,
			# it is used before eing even in the decoding dictionnary. No worries though, just use the concatenation of first char to previous sequence
			sequence = previous + previous[0]
			word += sequence
			if len(symbols) < 1<<BITS_USED:
				symbols.append(sequence)
			
		previous = sequence
	
	# NOTE : keep in mind that we are decompressing, so we are not iterating character by character like in encode(), but sequence by sequence
	
	return word






