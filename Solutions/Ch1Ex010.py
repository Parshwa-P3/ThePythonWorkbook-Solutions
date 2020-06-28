# Ch1Ex010.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 10
# Title: Arithmetic

import math

def main():
	a = int(input("a = "))
	b = int(input("b = "))

	print("Sum =        %d" % (a + b))
	print("Difference = %d" % (a - b))
	print("Product =    %d" % (a * b))
	print("Quotient =   %.4f" % (a / b))
	print("Remainder =  %d" % (a % b))
	print("Log =        %.4f" % (math.log10(a)))
	print("Power =      %d" % (math.pow(a, b)))

if __name__ == "__main__": main()