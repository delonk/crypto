import binascii
for x in range (0, 256):
	hexstring = hex(0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736 ^ x).rstrip("L").lstrip("0x")
	print hexstring
	#clean = '%x' %  hexstring
	#print clean
	print binascii.a2b_hex(hexstring)
