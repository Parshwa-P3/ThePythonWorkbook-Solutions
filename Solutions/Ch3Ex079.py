# Ch3Ex079.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 79
# Title: Maximum Integer

from random import randint

def main():
	maximum = randint(1, 100)
	print(maximum)
	updateCount = 0

	for i in range(100):
		number = randint(1, 100)
		print(number, end="")
		if number > maximum:
			maximum = number
			updateCount += 1
			print(" <- Update", end="")
		print()

	print("Maximum Number: %d" % maximum)
	print("Updates: %d" % updateCount)

if __name__ == "__main__": main()