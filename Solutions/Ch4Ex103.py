# Ch4Ex103.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 103
# Title: Magic Dates

from Ch4Ex100 import daysInMonth

def isMagicDate(dd, mm, YY):
	return (dd * mm) == (YY % 100)

def main():
	print("Magic Dates in any Century:")
	for i in range(100):
		yy = 1900 + i
		for j in range(12):
			mm = j + 1
			for k in range(daysInMonth(mm, yy)):
				dd = k + 1
				if isMagicDate(dd, mm, yy):
					print("%02d-%02d-%04d" % (dd, mm, yy), end="  ")
		print()			

if __name__ == "__main__": main()