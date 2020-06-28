# Ch3Ex077.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 77
# Title: Binary to Decimal

def main():
	binNum = input("Binary Number: ")
	decNum = count = 0

	for c in binNum[::-1]:
		decNum += int(c) * (2 ** count)
		count += 1

	print("Decimal Number: %d" % decNum)

if __name__ == "__main__": main()