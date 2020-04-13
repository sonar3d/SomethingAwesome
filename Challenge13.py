from Challenge11 import random_AES_key, detect_mode
from Challenge9 import padding
from Challenge7 import AES_encrypt, AES_decrypt
import string
import base64
global key
global u_id
global profile_list

key = random_AES_key()
u_id = 0
profile_list = []

def parse(string) :
	return dict(s.split('=', 1) for s in string.split('&'))

def profile_for(email) :
	global u_id
	global profile_list
	dictionary = {}
	email = email.replace('&', '')
	email = email.replace('=', '')
	dictionary['email'] = email
	dictionary['u_id'] = u_id
	
	dictionary['role'] = 'user'
	profile_list.append(dictionary)

	encoding = 'email' + '=' + email + '&' + 'u_id' + '=' + str(u_id) + '&' + 'role' + '=' + 'user'
	u_id += 1
	return encoding

def func_A(encoded) :
	return AES_encrypt(padding(encoded.encode(),16), key)

def func_B(encoded) :
	return AES_decrypt(encoded, key)

if __name__ == '__main__':
	print(parse("foo=bar&baz=qux&zap=zazzle"))
	print(profile_for('sona@me.com&role=admin'))
	print(profile_list)
	encoded = profile_for('sona@me.com&role=admin')
	provide = func_A(encoded)
	print(provide)
	parse = parse(func_B(provide).decode())
	print(parse)