# Ch4Ex094.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 94
# Title: Random Password

from random import randint

def randomPassword():
	l = randint(7, 10)
	ps = ''
	for i in range(l): ps += chr(randint(33, 127))
	
	return ps

def main():
	print("Random Password: %s" % randomPassword())

if __name__ == "__main__": main()