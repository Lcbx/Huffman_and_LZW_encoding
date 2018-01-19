import random
import string
import LZW
import huffman

#alphabet_length = random.randint(2,26)
#length = random.randint(4,14)
#word = ""
#for c in xrange(length):
#	word += string.ascii_uppercase[random.randint(0,alphabet_length-1)]





word = "Within two years the Court in Sherbert v. Verner 220 extended the line of analysis to require a religious exemption from a secular, regulatory piece of economic legislation."

code = LZW.encode(word)
print str(code) + "\n" + str(len(code))
word = LZW.decode(code)
print word + "\n" + str(len(word))

code = huffman.encode(word)
print code + "\n" + str(len(code))
word = huffman.decode(code)
print word + "\n" + str(len(word))