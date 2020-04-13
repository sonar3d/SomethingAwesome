import random
import secrets 
import math
import base64
from Challenge12 import encryption_constant_key, break_unknown_key, determine_block_size
from Challenge11 import random_AES_key, detect_mode
from Challenge9 import padding
from Challenge7 import AES_encrypt, AES_decrypt
global key
key = random_AES_key()
global string
global prefix
string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
prefix = secrets.token_bytes(random.randint(1, 15))

def prepend_random_bytes(prefix, byte_string) :
	return prefix + byte_string

def find_prefix_len() :
	first_block = b''
	for x in range(17) :
		encrypted = encryption_constant_key(prepend_random_bytes(prefix, b'A' * x), string)
		if first_block == encrypted[0:16] :
			return (16 - x+1)
		first_block = encrypted[0:16]
	return -1

def modified_encryption_constant_key(data_bytes) :
	append_bytes = base64.b64decode(string)
	input_bytes = prefix + data_bytes + append_bytes
	i = padding(input_bytes, 16)
	if len(i) % 16 != 0 :
		raise ValueError("input_bytes arent padded correctly")
	return AES_encrypt(i, key)
'''
#attempted to do with random number of bytes with no restrictions but could not find a way
#not sure if this is right
def find_randstr_length() :
	prev = b''
	for x in range(51) :
		encrypted = encryption_constant_key(prepend_random_bytes(b'A' * x), string)
	
		if x > 0 and prev == encrypted[:math.floor(x / 16)*16+16] :
			return x
		prev = encrypted[:math.floor(x / 16)*16+16]
		#[:math.floor(x / 16)*16+16]
	return -1
'''
def modified_break_unknown_key() :
	prefix_len = find_prefix_len()
	block_size = determine_block_size("")
	print(f'block size = {block_size}')
	# 2. detect mode 
	encrypted = modified_encryption_constant_key("my bytes are here: Lady Gaga".encode())
	print(detect_mode(encrypted*2))
	# 3. make input 1 byte short of block length
	print(string)
		
	dictionary = {}
	found_unknown_bytes = b''
	for b in range(int(len(string)/block_size)) : 
		
		#1 to 17
		for x in range(1, 17) :
				
			#b is number of blocks in
			input_bytes = b'A' * (block_size - x) 
				
			encrypted = modified_encryption_constant_key(input_bytes)
			start = b*block_size + prefix_len
			end = start + block_size
			current_block = encrypted[start : end]
			# 4. Make dictionary of all possible inputs 256
			
			for i in range(256) :
				u = input_bytes + found_unknown_bytes + chr(i).encode()
				dictionary[u] = chr(i)
				if modified_encryption_constant_key(u)[start : end] == current_block :
					found_unknown_bytes += chr(i).encode()
					print(found_unknown_bytes)
					break
	return found_unknown_bytes

if __name__ == '__main__':

	print(find_prefix_len())
	#string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
	print(modified_break_unknown_key().decode())
