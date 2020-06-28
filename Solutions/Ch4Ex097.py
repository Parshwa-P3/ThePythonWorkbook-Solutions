# Ch4Ex097.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 97
# Title: Random Good Password

from Ch4Ex094 import randomPassword
from Ch4Ex096 import isGoodPassword

def main():
	c = 1

	while True:
		s = randomPassword()
		if isGoodPassword(s):
			print("Good Password:", s)
			print("Attempts: %d" % c)
			break
		c += 1

if __name__ == "__main__": main()