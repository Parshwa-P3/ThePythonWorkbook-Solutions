# Ch4Ex083.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 83
# Title: Shipping Calculator

def calcCharge(numItems):
	totalCharge = 0
	singleCharge = 10.95
	incrementalCharge = 2.95
	
	while numItems > 1:
		totalCharge += incrementalCharge
		numItems -= 1
	
	totalCharge += singleCharge

	return totalCharge

def main():
	numItems = int(input("Number of Items: "))
	print("Charges: $% 6.2f" % calcCharge(numItems))

if __name__ == "__main__": main()