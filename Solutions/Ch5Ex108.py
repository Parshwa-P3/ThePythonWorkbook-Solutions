# Ch5Ex108.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 108
# Title: Negatives, Zeroes and Positives

def inputIntList():
	print("Enter the integers: [blank to stop]")
	ip = input()
	nums = []
	while ip != "":
		nums.append(int(ip))
		ip = input()
	return nums

def separateIntegers():
	nums = inputIntList()
	negs = []
	zeros = []
	poses = []

	for n in nums:
		if n < 0: negs.append(n)
		elif n == 0: zeros.append(n)
		elif n > 0: poses.append(n)
	
	print("\nSeparated Integers:")
	for n in negs: print(n)
	for n in zeros: print(n)
	for n in poses: print(n)

def main(): separateIntegers()

if __name__ == "__main__": main()