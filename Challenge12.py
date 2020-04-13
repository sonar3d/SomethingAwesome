from Challenge11 import random_AES_key, detect_mode
from Challenge9 import padding
from Challenge7 import AES_encrypt, AES_decrypt
import base64
global key
key = random_AES_key()

def encryption_constant_key(data_bytes, append_64) :
	append_bytes = base64.b64decode(append_64)
	input_bytes = data_bytes + append_bytes
	i = padding(input_bytes, 16)
	if len(i) % 16 != 0 :
		raise ValueError("input_bytes arent padded correctly")
	return AES_encrypt(i, key)

def determine_block_size(append_string) :
	#1. to discover block size 
	for i in range(1, 20) :
		encrypted = encryption_constant_key(("A" * i).encode(), append_string)
		if i == 1: length = len(encrypted)
		if len(encrypted) != length :
			block_size = i
			return block_size
		length = len(encrypted)
	return 0

def break_unknown_key(string) :
	block_size = determine_block_size("")
	print(f'block size = {block_size}')
	# 2. detect mode 
	encrypted = encryption_constant_key("my bytes are here: Lady Gaga".encode(), string)
	print(detect_mode(encrypted*2))
	# 3. make input 1 byte short of block length

		
	dictionary = {}
	found_unknown_bytes = b''
	for b in range(int(len(string)/block_size)) : 
		
		#1 to 17
		for x in range(1, 17) :
				
			#b is number of blocks in
			input_bytes = b'A' * (block_size - x) 
				
			encrypted = encryption_constant_key(input_bytes, string)
				
			current_block = encrypted[b*block_size : b*block_size +block_size]
			# 4. Make dictionary of all possible inputs 256
				
			for i in range(256) :
				u = input_bytes + found_unknown_bytes + chr(i).encode()
				dictionary[u] = chr(i)
				if encryption_constant_key(u, string)[b*block_size : b*block_size +block_size] == current_block :
					found_unknown_bytes += chr(i).encode()
					break
	return found_unknown_bytes

if __name__ == '__main__':
	string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
	
	print(f'string = {break_unknown_key(string).decode()}')
