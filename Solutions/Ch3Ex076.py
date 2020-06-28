# Ch3Ex076.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 76
# Title: Prime Factors

def main():
	num = int(input("Number: "))

	fact = 2
	factorsList = []

	while fact <= num:
		if num % fact == 0:
			factorsList.append(str(fact))
			num /= fact
		else:
			fact += 1

	print("Factors:", ", ".join(factorsList))

if __name__ == "__main__": main()