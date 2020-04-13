from Challenge2 import fixed_XOR, string_to_hex, string_to_bytes
from Challenge3 import single_char_xor
from Challenge5 import repeating_key_XOR, repeat_to_length
import base64

def base64_to_bytes(s) :
	return base64.b64decode(s)

#find number of differing bits between 2 strings
def HammingDist(s1, s2) :

	# convert strings to hex
	S1 = string_to_hex(s1)
	S2 = string_to_hex(s2)

	# xor strings 
	xored = fixed_XOR(s1, s2)

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
#step 6 takes in list and transposes it
def transpose_list(block_lists, keysize) :

	new_blocks_list = []

	for i in range(keysize) :
		new_block = b''

		for block in block_lists :
			new_block = new_block + block[i:i+1]

		new_blocks_list.append(new_block)
		

	return new_blocks_list
#step 7, 8
def solve_blocks(blocks) :

	solved = ''
	decrypt = []
	for block in blocks:
		decrypt_section, char = single_char_xor(block.hex()) 
		decrypt_section = base64.b64encode(decrypt_section.encode())
		decrypt_section = decrypt_section.decode('ascii')
		decrypt.append(decrypt_section)
		solved = solved + char
		print(f'key in c6 = {solved}')

	
	dec = []
	first = 1
	for block in blocks:
		if first == 1 :
			d = repeating_key_XOR(block.decode(), solved)
			dec.append(d)
		first = 0
	print(f'key from c6 is {dec}')

	return solved
def key_from_contents(contents) :
	KEYSIZE = 2
	string1 = ''
	string2 = ''
	string3 = ''
	string4 = ''
	entry = {}
	#print('doing string\n\n')

	byte_contents = base64_to_bytes(contents)
	for i in range(2, 41) :
		KEYSIZE = i
		string1 = byte_contents[0:i].decode()
		string2 = byte_contents[i:2*i].decode()
		string3 = byte_contents[2*i:3*i].decode()
		string4 = byte_contents[3*i:4*i].decode()
		#Part 3 ######################
		ham = HammingDist(string1, string2)/KEYSIZE 
		ham2 = HammingDist(string1, string3)/KEYSIZE
		ham3 = HammingDist(string1, string4)/KEYSIZE
		ham4 = HammingDist(string2, string3)/KEYSIZE
		ham5 = HammingDist(string2, string4)/KEYSIZE
		ham6 = HammingDist(string3, string4)/KEYSIZE
		ham_avg = (ham + ham2 + ham3 + ham4 + ham5 + ham6)/6
		entry[i] = ham_avg
	entry = {k: v for k, v in sorted(entry.items(), key=lambda item: item[1])}
	final_keysize = list(entry.keys())[0]

	################################################
	#### Part 5 break into keysize chunks ##########
	################################################
	split_contents = [byte_contents[i:i+final_keysize] for i in range(0, len(byte_contents), final_keysize)]

	#Part 6 transposing blocks############
	c6_version_transp = transpose_list(split_contents, final_keysize)

	print(f'len of trans = {len(c6_version_transp)}')
	########### Part 7 ###########################
	c6_decoded = solve_blocks(c6_version_transp) 

	return c6_decoded

def decode(contents, key) :
	c = (base64_to_bytes(contents)).decode()
	return (repeating_key_XOR(c, key))

def main() :
	f=open("c6_data.txt", "r")
	contents = f.readlines()
	contents = ''.join(contents)
	key = key_from_contents(contents)
	print(f'key = {key}')
	print(f'length of key found = {len(key)}')
	print(decode(contents, key))
	# program produces "Terminator X:'Bring the noise"
	# found that this is correct key "Terminator X: Bring the noise"

if __name__ == "__main__":
	main()
