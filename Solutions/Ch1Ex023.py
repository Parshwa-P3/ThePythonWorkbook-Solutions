# Ch1Ex023.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 23
# Title: Area of a Regular Polygon

import math as m

def main():
	numSides = float(input("No. of Sides: ")) 
	sideLen = float(input("Length of Side (cm): "))

	area = (numSides * sideLen * sideLen) / (4 * m.tan(m.pi / numSides))

	print("Area: %.2f cm²" % area)

if __name__ == "__main__": main()