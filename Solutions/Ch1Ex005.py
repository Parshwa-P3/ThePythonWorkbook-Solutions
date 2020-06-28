# Ch1Ex005.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 5
# Title: Bottle Deposits

def main():
	lessThan1 = int(input("Less than 1 L: "))
	moreThan1 = int(input("More than 1 L: "))

	refund = (0.1 * lessThan1) + (0.25 * moreThan1)

	print("Refund: $" + str(refund))

if __name__ == "__main__": main()