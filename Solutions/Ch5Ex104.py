# Ch5Ex104.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 104
# Title: Sorted Order

def inputNumList():
	print("Enter the numbers: [0 to stop]")
	ip = int(input())
	nums = []
	while ip != 0:
		nums.append(ip)
		ip = int(input())
	return nums

def sortedOrder():
	nums = inputNumList()
	print("\nSorted numbers:")
	for i in sorted(nums): print(i)

def main(): sortedOrder()

if __name__ == "__main__": main()