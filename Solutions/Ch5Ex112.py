# Ch5Ex112.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 112
# Title: Below and Above Average

from Ch5Ex104 import inputNumList

def calcAvg(nums):
	return sum(nums) / float(len(nums))

def separateByAvg(nums):
	avg = calcAvg(nums)
	below = []
	equal = []
	above = []

	for n in nums:
		if n < avg: below.append(n)
		if n == avg: equal.append(n)
		if n > avg: above.append(n)
	
	print("\nBelow Average: ", end="")
	for n in below: print(n, end=" ")
	print("\nEqual to Average: ", end="")
	for n in equal: print(n, end=" ")
	print("\nAbove Average: ", end="")
	for n in above: print(n, end=" ")

def main():
	nums = inputNumList()
	separateByAvg(nums)

if __name__ == "__main__": main()