from Challenge1 import hexdecode
import codecs
import binascii
import string 

#get rid of non-alphanmeric chars
def strip(s) :
	new = ""
	for c in s:
		if c.isalpha() or c.isnumeric():
			new = new + c
	return new

#returns hex from string input 
def string_to_hex(string) :
	return string.encode().hex()

def string_to_bytes(string) :
	return bytes.fromhex(string.encode().hex())

#returns STRING utf-8 of xored hex strings
def fixed_XOR(str1, str2) :
	
	if not all(c in string.hexdigits for c in str1) :
		str1 = string_to_hex(str1)
	if not all(c in string.hexdigits for c in str2) :
		str2 = string_to_hex(str2)

	A = bytes.fromhex(str1)
	B = bytes.fromhex(str2)
	
	return ("".join(chr(a ^ b) for a, b in zip(A, B)))
'''
test:
x = fixed_XOR('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')
'''