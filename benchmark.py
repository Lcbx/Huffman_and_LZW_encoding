import random
import string
import LZW

alphabet_length = random.randint(2,26)
length = random.randint(4,14)
word = ""
for c in xrange(length):
	word += string.ascii_uppercase[random.randint(0,alphabet_length-1)]

code = LZW.encode(alphabet_length,word)

print("word : " + word )
print("code :"),
for t in code :
	print(t),
print

word = LZW.decode(alphabet_length, code)
print("word : " + word )