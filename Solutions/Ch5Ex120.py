# Ch5Ex120.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 120
# Title: Is a List already in Sorted Order?

from Ch5Ex104 import inputNumList

def isListSorted(nums):
	if len(nums) < 2: return True
	for i in range(len(nums) - 2):
		if nums[i] > nums[i + 1] and nums[i + 1] < nums[i + 2]:
			return False
		elif nums[i] < nums[i + 1] and nums[i + 1] > nums[i + 2]:
			return False
	return True

def main():
	nums = inputNumList()
	print("List:", nums, end=" ")
	if isListSorted(nums): print("is Sorted")
	else: print("is Not Sorted")

if __name__ == "__main__": main()