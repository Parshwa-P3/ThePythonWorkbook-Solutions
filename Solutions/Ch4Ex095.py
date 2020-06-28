# Ch4Ex095.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 95
# Title: Random License Plate

from random import randint

def randomLicensePlate():
	letters = [65, 90]
	digits = [48, 57]
	lp = ''

	if randint(1, 100) > 50:
		for i in range(3):
			lp += chr(randint(letters[0], letters[1]))
		for i in range(3):
			lp += chr(randint(digits[0], digits[1]))
	else:
		for i in range(4):
			lp += chr(randint(digits[0], digits[1]))
		for i in range(3):
			lp += chr(randint(letters[0], letters[1]))

	return lp

def main():
	print("Random License Plate: %s" % randomLicensePlate())

if __name__ == "__main__": main()