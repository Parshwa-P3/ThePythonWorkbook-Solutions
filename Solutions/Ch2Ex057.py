# Ch2Ex057.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 57
# Title: Is it a Leap Year

def main():
	yy = int(input("Year: "))

	leap = True

	if yy % 400 == 0: leap = True
	elif yy % 100 == 0: leap = False
	elif yy % 4 == 0: leap = True
	else: leap = False

	if leap: print("Leap Year")
	else: print("Not a Leap Year")

if __name__ == "__main__": main()