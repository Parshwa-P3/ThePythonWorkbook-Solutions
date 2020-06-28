# Ch3Ex075.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 75
# Title: Greatest Common Divisor

def main():
	m = int(input("m = "))
	n = int(input("n = "))

	div = m if m < n else n
	while m % div != 0 or n % div != 0: div -= 1

	print("GCD = %d" % div)

if __name__ == "__main__": main()