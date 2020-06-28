# Ch3Ex070.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 70
# Title: Caesar Cipher

def main():
	az = "abcdefghijklmnopqrstuvwxyz" 
	AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	plaintext = input("Plaintext: ")
	shift = int(input("Shift Amount: "))
	ciphertext = []

	for c in plaintext:
		if c.isalpha():
			if c.islower():
				ciphertext.append(az[(az.find(c) + shift) % 26])
			elif c.isupper():
				ciphertext.append(AZ[(AZ.find(c) + shift) % 26])
		else:
			ciphertext.append(c)

	print(''.join(ciphertext))

if __name__ == "__main__": main()