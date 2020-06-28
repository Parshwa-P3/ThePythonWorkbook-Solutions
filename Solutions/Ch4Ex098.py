# Ch4Ex098.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 98
# Title: Hexadecimal and Decimal digits

ALPHA = ['A', 'B', 'C', 'D', 'E', 'F']
DIGIT = [str(i) for i in range(10)]

def hexToDec(s):
	if s in DIGIT:
		return int(s)
	elif s.upper() in ALPHA:
		return 10 + ALPHA.index(s.upper())
	else:
		print("Invalid input!")

def decToHex(s):
	s = str(s)
	if s in DIGIT:
		return s
	elif int(s) in range(10, 16):
		return ALPHA[int(s) - 10]
	else:
		print("Invalid input!")

def main():
	print("Hex: F  Dec: %s" % hexToDec('F') )
	print("Dec: 13 Hex: %s" % decToHex('13'))

if __name__ == "__main__": main()