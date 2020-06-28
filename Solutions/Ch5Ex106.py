# Ch5Ex106.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 106
# Title: Remove Outliers

from Ch5Ex104 import inputNumList

def removeOutliers(vals, n):
	if len(vals) <= 2 * n:
		print("List too small!")
		return
	newVals = sorted(vals)
	newVals = newVals[n:-n]
	print("\nNew List: ", end="")
	for i in newVals: print(i, end=" ")
	print("\nOriginal List: ", end="")
	for i in vals: print(i, end=" ")

def main():
	nums = inputNumList()
	n = int(input("\nn = "))
	removeOutliers(nums, n)

if __name__ == "__main__": main()