import random
import string
import LZW
import huffman

#alphabet_length = random.randint(2,26)
#length = random.randint(4,14)
#word = ""
#for c in xrange(length):
#	word += string.ascii_uppercase[random.randint(0,alphabet_length-1)]





word = "Students who pursue the Latin major read a wide variety of authors and can expect to achieve a high level of competency in the ancient language of the Romans. Coursework includes such favorites as Vergil, Ovid, Cicero, Julius Caesar, and Catullus, but students can expect to be able to read other authors like the historians (Livy, Sallust, and Tacitus) and genres like lyric, satire, and drama.  To support Latin majors as they pursue their educational goals, CANES provides annual scholarship opportunities. We also offer a summer study abroad program led by members of our faculty. Learn more under Resources and Scholarships. For those who are interested in teaching Latin at the secondary level, the School of Education offers certification. Students of this program take Latin courses in our department, while receiving their teacher training in the School of Education. "

code = LZW.encode(word)
print str(code) + "\n" + str(len(code))
word = LZW.decode(code)
print word + "\n" + str(len(word))

code = huffman.encode(word)
print code + "\n" + str(len(code))
word = huffman.decode(code)
print word + "\n" + str(len(word))