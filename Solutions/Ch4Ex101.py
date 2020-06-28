# Ch4Ex101.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 101
# Title: Reduce a Fraction to lowest terms

def calcGCD(num1, num2):
	gcd = num1 if num1 < num2 else num2
	while num1 % gcd != 0 or num2 % gcd != 0: gcd -= 1
	return gcd

def reduceFrac(num, den):
	gcd = calcGCD(num, den)
	num = num / gcd
	den = den / gcd

	return num, den

def main():
	num, den = [int(i) for i in input("Enter a Fraction (p/q) (no spaces):\n").split('/')]

	newNum, newDen = reduceFrac(num, den)
	print("Reduced Fraction: %d/%d" % (newNum, newDen))

if __name__ == "__main__": main()