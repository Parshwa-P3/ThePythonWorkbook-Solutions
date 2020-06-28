# Ch5Ex121.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 121
# Title: Count the Elements

def countRange(nums, rMin, rMax):
	count = 0
	for n in nums:
		if n >= rMin and n < rMax: count += 1
	return count

def main():
	tests = [
		[[1, 2, 3, 4, 5], 1, 4],
		[[1, 2, 3, 4, 5], 2, 4],
		[[1.1, 1.2, 1.3, 1.4, 1.5], 1, 2],
		[[1.1, 1.2, 1.3, 1.4, 1.5], 1, 1.5],
		[[1.5, 1.7, 1.9, 2], 1, 2],
	] # Test Cases

	i = 1
	for t in tests: 
		print("Test case %d:" % i)
		print("List:", t[0], ", min:", t[1], ", max:", t[2], "=> count:", countRange(t[0], t[1], t[2]))
		i += 1

if __name__ == "__main__": main()