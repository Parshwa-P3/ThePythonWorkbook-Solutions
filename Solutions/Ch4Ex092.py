# Ch4Ex092.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 92
# Title: Is a Number Prime?

def isPrime(n):
	if n <= 1: return False
	
	for i in range(2, int(n**0.5)):
		if n % i == 0: return False
	
	return True

def main():
	n = int(input("Number: "))
	if isPrime(n): print("%d is prime" % n)
	else: print("%d is not prime" % n)

if __name__ == "__main__": main()