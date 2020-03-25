from Challenge3 import xor_check, freq_match_score

f=open("challenge4Data.txt", "r")
contents = f.readlines()
s = '\n'.join(contents)

x = []
for line in contents:
	#L = line.encode().hex()
	print(line)
	x.append(xor_check(line)[0])

best_score = 0
for line in x:
	if freq_match_score(line) > best_score: 
		best_score = freq_match_score(line)
		english = line

print(line)