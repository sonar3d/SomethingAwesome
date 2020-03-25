from Challenge2 import fixed_XOR, string_to_hex
from Challenge3 import xor_check, xor_check_key
from Challenge5 import repeating_key_XOR, repeat_to_length
import base64
import textwrap

f=open("challenge4Data.txt", "r")
contents = f.readlines()
contents = ''.join(contents)
print(contents)
def base64_to_bytes(s) :
	return base64.base64decode(s)

#find number of differing bits between 2 strings
def HammingDist(s1, s2) :

	# convert strings to hex
	S1 = string_to_hex(s1)
	S2 = string_to_hex(s2)

	# xor strings 
	xored = fixed_XOR(S1, S2)

	# convert to bits
	xored = (''.join(format(i, 'b') for i in bytearray(xored, encoding ='utf-8')))


	dist = 0
	
	#add all bits (8*number of differing bits) that are different
	length_diff = abs(len(S1) - len(S2))
	dist+= length_diff*8

	#add all 1's in xored as that represents different 
	for bit in xored :
		if bit == '1': dist+= 1

	return dist


print(f'two spaces: {HammingDist("", "  ")}')
print(f'difference for testing:  {HammingDist("this is a test", "wokka wokka!!!")}')

def key_from_contents(contents) :
	KEYSIZE = 2
	string1 = ''
	string2 = ''
	string3 = ''
	string4 = ''
	entry = {}
	print('doing string\n\n')
	for i in range(2, 41) :
		KEYSIZE = i
		for x in range(i) :
			string1 += contents[x] 
			string2 += contents[x+i] 
		ham = HammingDist(string1, string2)
		entry = {i: ham}
	entry = {k: v for k, v in sorted(entry.items(), key=lambda item: item[1])}
	final_keysize = list(entry.keys())[0]

	split_contents = textwrap.wrap(contents, final_keysize)

	new_blocks = []
	for x in range(final_keysize) :
		new_blocks.append('')
	#transposing blocks
	for element in split_contents:
		x = 0
		#add each letter to a different block in new_blocks list 
		for letter in element :
			new_blocks[x] += letter
			x+=1
	print(new_blocks)
	print("DECODING NOW HOPEFULLY")

	decoded_blocks = []
	key = ''
	for block in new_blocks:
		hex_int = int(block,16)
		hex_str = hex(hex_int)
		print(f'block = {block} hex_int = {hex_int} hex_str = {hex_str}')
		decoded = xor_check(hex_str)
		decoded_blocks.append(decoded)
		key += xor_check_key(block)
	print(decoded_blocks)
	return key

print(key_from_contents(contents))

