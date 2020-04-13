from Challenge2 import fixed_XOR, string_to_hex, strip

def repeat_to_length(string, length):
    return (string * (int(length/len(string))+1))[:length]

def repeating_key_XOR(s, key) :
	L = len(s)
	rep_key = repeat_to_length(key, L)
	#print(rep_key)
	return fixed_XOR(s, rep_key)

#returns bytes from bytes
def fixed_bytes_XOR(A, B) :
	
	return ("".join(chr(a ^ b) for a, b in zip(A, B))).encode()

def repeating_key_bytes_XOR(input_bytes, key) :
	L = len(input_bytes)
	rep_key = repeat_to_length(key, L)
	#print(rep_key)
	return fixed_bytes_XOR(input_bytes, rep_key)

encrypt = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
s1 = string_to_hex((encrypt))
s2 = string_to_hex(("ICE"))

finalS = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

x = repeating_key_XOR(s1, s2)
#print(x)
diff = len(finalS) - len(x)
#print(f'length diff is {diff}')
'''
#print(f"x length = {len(x)} and expected length is {len(finalS)}")
for i in range(len(x)) :
	if x[i] != finalS[i] :
		#print(f"i = {i} and character = {x[i]}")
		#print("uh ohhh")
'''
