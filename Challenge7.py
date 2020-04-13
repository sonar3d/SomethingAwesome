from Crypto.Cipher import AES
from base64 import b64decode, b64encode


def AES_decrypt(input_bytes, key_bytes) :
	aes = AES.new(key_bytes, AES.MODE_ECB)
	return aes.decrypt(input_bytes)

def AES_encrypt(input_bytes, key_bytes) :
	aes = AES.new(key_bytes, AES.MODE_ECB)
	return aes.encrypt(input_bytes)


if __name__ == '__main__':
	f = open('c7.txt')
	f = f.read()
	key = "YELLOW SUBMARINE".encode()
	input_bytes = b64decode(f)
	print(AES_decrypt(input_bytes, key).decode())