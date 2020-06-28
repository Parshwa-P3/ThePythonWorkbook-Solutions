# Ch1Ex031.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 31
# Title: Sum of the digits of a number

def main():
	N = int(input("4-digit Number: "))

	s = 0
	while N > 0:
		s += N % 10
		N = N // 10

	print("Sum of digits: %d" % s)

if __name__ == "__main__": main()