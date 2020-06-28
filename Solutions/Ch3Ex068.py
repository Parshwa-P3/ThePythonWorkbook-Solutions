# Ch3Ex068.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 68
# Title: Parity Bits

import re

def main():
	while True:
		s = input("Enter String: ")
		if s == "":
			break
		elif len(s) != 8 or not re.match(r'^[01]+$', s):
			print("ERR!")
			break

		c = s.count('1')
		p = c % 2
		print("Parity Bit: %d" % p)

if __name__ == "__main__": main()