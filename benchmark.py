import LZW
import huffman

import string
import random
from datetime import datetime


seed = datetime.now()
random.seed(seed)
#print "seed : " + str(seed)


alphabet_length = 15 #random.randint(2,26)
length =  500 #random.randint(5,500)
word = ""
for c in xrange(length):
	word += string.ascii_uppercase[random.randint(0,alphabet_length-1)]



	
	
def test(algorithm, word = 
"""Hello darkness, my old friend
I've come to talk with you again
Because a vision softly creeping
Left its seeds while I was sleeping
And the vision that was planted in my brain
Still remains
Within the sound of silence
In restless dreams I walked alone
Narrow streets of cobblestone
'Neath the halo of a street lamp
I turned my collar to the cold and damp
When my eyes were stabbed by the flash of a neon light
That split the night
And touched the sound of silence"""):
	
	print "    " + algorithm.__name__
	code = algorithm.encode(word)
	print "\t code : \n" + str(code) + "\n" + str(len(code)/8) + "\n"
	result = algorithm.decode(code)
	print "\t result of decoding : \n" + result + "\n" + str(len(result)) + "\n"
	

test(LZW)

test(huffman)