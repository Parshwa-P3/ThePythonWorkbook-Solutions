# Ch5Ex126.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 126
# Title: Generate all Sublists of a List

def generateSublists(inputList):
	sublists = [[]]
	if len(inputList) > 0:
		for i in range(len(inputList)):
			for j in range(i + 1, len(inputList) + 1):
				sublists.append(inputList[i: j])
	return sublists

def main():
	tests = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4]] # Test Cases
	
	for i in range(len(tests)):
		print("Test Case %d:" % (i + 1))
		print("  Full List:", tests[i])
		print("  Sublists:", generateSublists(tests[i]))

if __name__ == "__main__": main()