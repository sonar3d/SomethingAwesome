import random
import secrets 
import math
import base64
from Challenge12 import encryption_constant_key, break_unknown_key, determine_block_size
from Challenge11 import random_AES_key, detect_mode
from Challenge9 import padding
from Challenge10 import CBC_encrypt, CBC_decrypt
global key
global IV
key = random_AES_key()
IV = random_AES_key()

def sandwich(string) :
	#The function should quote out the ";" and "=" characters.
	string = string.replace(';', '')
	string = string.replace('=', '')
	s = b"comment1=cooking%20MCs;userdata=" + string.encode() + b";comment2=%20like%20a%20pound%20of%20bacon"
	s = padding(s, 16)
	return CBC_encrypt(IV, s, key)

def is_admin(encrypted_bytes) :
	s = CBC_decrypt(IV, encrypted_bytes, key).decode()
	Dictionary = dict(string.split('=', 1) for string in s.split(';'))
	if 'admin' in list(Dictionary.keys()) :
		if Dictionary['admin'] == 'true' : return True
	return False

def bit_flipping_attack(ciphertext) :
	x = ciphertext + b'A' * 16 + b'admin=true'
	x = padding(x, 16)
	if len(x) % 16 != 0 :
		raise ValueError("input_bytes arent padded correctly")

	return x

def test_16_1() :
	e = sandwich("mystring")
	assert (is_admin(e)) == False
	e = sandwich(";admin=true;")
	assert (is_admin(e)) == False

def test_16_2() :
	e = sandwich("mystring")
	assert (is_admin(e)) == False
	e = sandwich(";admin=true;")
	assert (is_admin(e)) == False
	attacked = bit_flipping_attack(e)
	assert is_admin(attacked) == True

if __name__ == '__main__':
	
	test_16_1()
	test_16_2()