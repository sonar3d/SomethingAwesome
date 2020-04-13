import itertools
import pytest

def padding_valid(padded_string_bytes) :
	last = padded_string_bytes[-1]

	for i in range(1, last+1) :
		#print(i)
		#print(f'byte = {padded_string_bytes[-i]}')
		if padded_string_bytes[-i] != last :
			raise ValueError("input_bytes arent padded correctly")
	return padded_string_bytes[:-last]

def test_15_1() :
	assert padding_valid(b"ICE ICE BABY\x04\x04\x04\x04") == b"ICE ICE BABY"
def test_15_2() :
	with pytest.raises(ValueError, match=r"input_bytes arent padded correctly"):
		padding_valid(b"ICE ICE BABY\x05\x05\x05\x05") == b"ICE ICE BABY"
def test_15_3() :
	with pytest.raises(ValueError, match=r"input_bytes arent padded correctly"):
		padding_valid(b"ICE ICE BABY\x01\x02\x03\x04") == b"ICE ICE BABY"
if __name__ == '__main__':
	test_15_3()
	test_15_2()
	test_15_1()
	print("Test passed!!! wOooOoOO")

