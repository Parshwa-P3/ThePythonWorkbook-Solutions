# Ch1Ex032.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 32
# Title: Sort three numbers

def main():
	print("Enter numbers: ")
	numbers = list(map(int, input().strip().split()))

	for i in range(len(numbers) - 1):
		for j in range(1, len(numbers)):
			if numbers[j - 1] > numbers[j]:
				numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]

	print("Sorted: ")
	for n in numbers: print(str(n) + " ", end="")

if __name__ == "__main__": main()