# Ch4Ex100.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 100
# Title: Days in a Month

def isLeapYear(yy):
	leap = True

	if yy % 400 == 0: leap = True
	elif yy % 100 == 0: leap = False
	elif yy % 4 == 0: leap = True
	else: leap = False
	
	return leap

def daysInMonth(mm, yy):
	leap = isLeapYear(yy)
	
	if mm in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	elif mm in [4, 6, 9, 11]:
		return 30
	elif mm == 2:
		if leap: return 29
		else: return 28

def main():
	mm = int(input("Enter Month: "))
	yy = int(input("Enter Year:  "))
	print("Number of Days: %d" % daysInMonth(mm, yy))

if __name__ == "__main__": main()