# Ch5Ex125.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 125
# Title: Does a List contain a Sublist?

def isSublist(smaller, larger):
	result = True
	if len(smaller) == 0: result = True
	else:
		for i in range(len(larger) - len(smaller)):
			result = True
			if larger[i] == smaller[0]:
				for j in range(1, len(smaller)):
					if larger[i + j] != smaller[j]:
						result = False
	return result

def main():
	tests = [
		[list(range(5)), list(range(10))],
		[list(range(2, 5)), list(range(10))],
		[list(range(5)), list(range(2, 10))],
		[[1, 3, 2], list(range(5))],
		[[], list(range(5))],
		[[], []]
	] # Test Cases

	for i in range(len(tests)):
		print("Test case %d:" % (i + 1))
		print(tests[i][0], tests[i][1], "=> isSublist:",\
			 isSublist(tests[i][0], tests[i][1]))

if __name__ == "__main__": main()