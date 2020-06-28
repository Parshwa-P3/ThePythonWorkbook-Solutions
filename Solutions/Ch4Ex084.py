# Ch4Ex084.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 84
# Title: Median of Three Values

def findMedian(n1, n2, n3):
	a = sorted([n1, n2, n3])
	return a[1]

def main(): findMedian(12, 9, 15)

if __name__ == "__main__": main()