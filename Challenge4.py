from Challenge3 import xor_check, freq_match_score, score

f=open("challenge4Data.txt", "r")
contents = f.readlines()

def find_encrypted_string(contents) :
	x = []
	#print(contents)
	print("DECODING")
	for line in contents:
		#L = line.encode().hex()
		#print(xor_check(line))

		x.append(xor_check(line))
	print(x)
	best_score = 10000
	english = ""
	for line in x:
		if score(line) < best_score: 
			best_score = score(line)
			english = line
	#print(f'line = {line}')
	print("end")
	print(x[169])
	return english
print(f'english = {find_encrypted_string(contents)}')