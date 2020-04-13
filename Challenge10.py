from Challenge7 import AES_encrypt, AES_decrypt
from Challenge9 import padding
from Challenge5 import repeating_key_bytes_XOR, fixed_bytes_XOR
import base64
import string

def CBC_encrypt(IV, input_bytes, key) :
	split = [input_bytes[i:i+len(key)] for i in range(0, len(input_bytes), len(key))]
	prev_encrypt = IV
	if len(prev_encrypt) % 16 != 0 :
		raise ValueError("IV not multiple of 16")
	ciphertext = b''
	for block in split:
		x = fixed_bytes_XOR(prev_encrypt, block)
		if len(key) % 16 != 0 :
			raise ValueError("key not multiple of 16")
		x = AES_encrypt(x, key)
		prev_encrypt = x
		ciphertext += prev_encrypt
	return ciphertext

def CBC_decrypt(IV, input_bytes, key) :
	split = [input_bytes[i:i+len(key)] for i in range(0, len(input_bytes), len(key))]
	plaintext = b''
	prev = IV
	for block in split:
		#decrypt current block with key
		decode = AES_decrypt(block, key)
		#xor with previous ciphertext
		plaintext += fixed_bytes_XOR(decode, prev)
		prev = block
	return plaintext

if __name__ == '__main__':
	key = b'YELLOW SUBMARINE'
	#input_bytes = padding("Hozier From Eden", 16)
	input_bytes = "Hozier From Eden".encode()
	encode = AES_encrypt(input_bytes, key)
	decode = AES_decrypt(encode, key)
	#print(f'decoded is: {decode}')
	assert decode == b'Hozier From Eden'

	f = b''.join([base64.b64decode(line.strip()) for line in open("c10.txt").readlines()])
	IV = b'\x00' * 16
	decode = (CBC_decrypt(IV, f, key)).decode()
	print('plaintext')
	print(decode)