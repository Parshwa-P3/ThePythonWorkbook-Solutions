# Ch1Ex009.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 9
# Title: Compund Interest

def main():
	bal = float(input("Amount: $"))

	bal = bal + (0.04 * bal)
	print("\nAfter 1 year: 	$%.2f\n" % bal)
	bal = bal + (0.04 * bal)
	print("\nAfter 2 years: $%.2f\n" % bal)
	bal = bal + (0.04 * bal)
	print("\nAfter 3 years: $%.2f\n" % bal)

if __name__ == "__main__": main()