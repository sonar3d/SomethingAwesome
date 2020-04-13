from Challenge7 import AES_decrypt

def AES_ecb_detect(Cipher_bytes) :
	split_16 = [Cipher_bytes[i:i+16] for i in range(0, len(Cipher_bytes), 16)]
	if len(split_16) != len(set(split_16)):
		return 1
	else :
		return 0
		
if __name__ == '__main__':
	f = open('c8.txt')
	f = f.readlines()
	line = 0
	for ciphertext in f :
		
		c = bytes.fromhex(ciphertext)
		if AES_ecb_detect(c) :
			print(f'ciphertext = {ciphertext} \nline = {line}')
		line += 1