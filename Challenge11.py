import random
import secrets 
from Challenge7 import AES_encrypt, AES_decrypt
from Challenge10 import CBC_encrypt
from Challenge9 import padding
from Challenge8 import AES_ecb_detect

def random_AES_key() :
	return secrets.token_bytes(16)

def encryption_oracle(data_bytes) :
	input_bytes = secrets.token_bytes(random.randint(5, 10)) + data_bytes + secrets.token_bytes(random.randint(5, 10))
	i = padding(input_bytes, 16)
	if len(i) % 16 != 0 :
		raise ValueError("input_bytes arent padded correctly")
	if random.randint(0, 1) :
		return CBC_encrypt(random_AES_key(), i, random_AES_key())
	else :
		return AES_encrypt(i, random_AES_key())

def detect_mode(encrypted_bytes) :
	if AES_ecb_detect(encrypted_bytes) :
		return "Used AES ECB mode"
	else :
		return "Used CBC mode"

if __name__ == '__main__':

	#print(encryption_oracle((b"This is not jibberish" * 32)))
	print(detect_mode(encryption_oracle(b"a" * 64)))