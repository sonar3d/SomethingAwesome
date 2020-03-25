from Challenge2 import fixed_XOR, string_to_hex 
from string import ascii_lowercase
from langdetect import detect
import string

def freq_dict(string):	
	d = {}
	x = ''
	for i in range(len(string)) :
		if string[i].isalpha() :
			x = string[i].lower()
			if x in d.keys():
				d[x] += 1
			else:
				d[x] = 1
	for i in ascii_lowercase :
		if i not in d.keys() :
			d[i] = 0
	d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
	#print(d)
	return d

def index(s) :
	d = freq_dict(s)
	sum = 0
	for key in d :
		sum += (d[key] * (d[key] - 1) )
	if len(s) == 0 or len(s) == 1:
		return 0 
	return sum/(len(s)*(len(s) - 1)/26)

'''
#lower the score closer to expected english
def score(s) :
	L = len(s)
	d = freq_dict(s)
	#print(d)

	score_dict = {}
	score_dict['a'] = abs(d['a']*100/L - 8.167)
	score_dict['b'] = abs(d['b']*100/L - 1.492)
	score_dict['c'] = abs(d['c']*100/L - 2.202)
	score_dict['d'] = abs(d['d']*100/L - 4.253)
	score_dict['e'] = abs(d['e']*100/L - 12.702)
	score_dict['f'] = abs(d['f']*100/L - 2.228)
	score_dict['g'] = abs(d['g']*100/L - 2.015)
	score_dict['h'] = abs(d['h']*100/L - 6.094)
	score_dict['i'] = abs(d['i']*100/L - 6.966)
	score_dict['j'] = abs(d['j']*100/L - 0.153)
	score_dict['k'] = abs(d['k']*100/L - 1.292)
	score_dict['l'] = abs(d['l']*100/L - 4.025)
	score_dict['m'] = abs(d['m']*100/L - 2.40)
	score_dict['n'] = abs(d['n']*100/L - 6.749)
	score_dict['o'] = abs(d['o']*100/L - 7.507)
	score_dict['p'] = abs(d['p']*100/L - 1.929)
	score_dict['q'] = abs(d['q']*100/L - 0.095)
	score_dict['r'] = abs(d['r']*100/L - 5.987)
	score_dict['s'] = abs(d['s']*100/L - 6.327)
	score_dict['t'] = abs(d['t']*100/L - 9.356)
	score_dict['u'] = abs(d['u']*100/L - 2.758)
	score_dict['v'] = abs(d['v']*100/L - 0.978)
	score_dict['w'] = abs(d['w']*100/L - 2.560)
	score_dict['x'] = abs(d['x']*100/L - 0.150)
	score_dict['y'] = abs(d['y']*100/L - 1.994)
	score_dict['z'] = abs(d['z']*100/L - 0.077)
	#print(score_dict)
	
	Sum = 0

	for value in d.values() :
		Sum += value
	#print(f'sum = {Sum}')
	return Sum 
'''
#perfect score is 12 
#checks if the 6 most frequent and 6 least frequent letters are the same as expected in English
def freq_match_score(st) :
	dic = freq_dict(st)
	score = 0
	i = 0
	for letter in dic.keys() :
		if i in range(0, 7) :
			if letter == 'v' or letter == 'j' or letter == 'k' or letter == 'x' or letter == 'q' or letter == 'z' :
				score += 1
		if i in range(21,27):
			if letter == 'e' or letter == 't' or letter == 'a' or letter == 'i' or letter == 'o' or letter == 'n' :
				score += 1
		i += 1
	return score

def xor_check(s) :
	d_index = {}
	array = []
	k = 0
	for i in ascii_lowercase :
		#xor for each character
		#print(f'\ni = {i}')
		#change length of i
		while len(i) < len(s) :
			i = i + i
		#change to hex and xor char against input string
		i = i.encode().hex()

		xored = fixed_XOR(i, s)

		#append xored string to array, array[0] should be xored from "a"
		array.append(xored)
		#find the index of this text  
		d_index[k] = abs(index(xored) - 1.73)
		k += 1
		#print(f'xored = {xored}\nindex = {d_index[k-1]}')

	#return min d_index value 
	#min = list(d_index.keys())[0]
	min = 1000
	j = 0 
	Key_Needed = 0
	
	for key in d_index :
		
		if d_index[key] == float(min) :
			if freq_match_score(array[Key_Needed]) < freq_match_score(array[j]) :
				Key_Needed = j
		
		if d_index[key] < float(min) :
			min = d_index[key]
			Key_Needed = j
		j+=1

	string = array[Key_Needed]


	final_key = chr(ord('`')+Key_Needed)

	return array[Key_Needed]

def xor_check_key(s) :
	d_index = {}
	array = []
	k = 0
	for i in ascii_lowercase :
		#xor for each character
		#print(f'\ni = {i}')
		#change length of i
		while len(i) < len(s) :
			i = i + i
		#change to hex and xor char against input string
		i = i.encode().hex()

		xored = fixed_XOR(i, s)

		#append xored string to array, array[0] should be xored from "a"
		array.append(xored)
		#find the index of this text  
		d_index[k] = abs(index(xored) - 1.73)
		k += 1
		#print(f'xored = {xored}\nindex = {d_index[k-1]}')

	#return min d_index value 
	#min = list(d_index.keys())[0]
	min = 1000
	j = 0 
	Key_Needed = 0
	
	for key in d_index :
		
		if d_index[key] == float(min) :
			if freq_match_score(array[Key_Needed]) < freq_match_score(array[j]) :
				Key_Needed = j
		
		if d_index[key] < float(min) :
			min = d_index[key]
			Key_Needed = j
		j+=1

	string = array[Key_Needed]


	final_key = chr(ord('`')+Key_Needed)

	return final_key

print(xor_check('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
print(xor_check_key('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))