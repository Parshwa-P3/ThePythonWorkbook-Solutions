# Ch4Ex093.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 93
# Title: Next Prime

from Ch4Ex092 import isPrime

def nextPrime(n):
	while True:
		n += 1
		if isPrime(n): return n		

def main():
	n = int(input("Number: "))
	print("Next Prime: %d" % nextPrime(n))

if __name__ == "__main__": main()