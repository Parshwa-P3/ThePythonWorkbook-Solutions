# Ch5Ex105.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 105
# Title: Reverse Order

from Ch5Ex104 import inputNumList

def reverseOrder():
	nums = inputNumList()
	print("\nReversed numbers:")
	for i in nums[::-1]: print(i)

def main(): reverseOrder()

if __name__ == "__main__": main()