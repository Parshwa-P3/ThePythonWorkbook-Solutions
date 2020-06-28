# Ch5Ex110.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 110
# Title: Perfect Numbers

from Ch5Ex109 import properDivisors

def isPerfect(n):
	divs = properDivisors(n)
	return sum(divs) == n

def main():
	low = int(input("Enter Lower bound: "))
	up = int(input("Enter Upper bound: "))
	print("Perfect Numbers:")
	for n in range(low, up + 1): 
		if isPerfect(n): print(n, end=" ")

if __name__ == "__main__": main()