# Ch1Ex022.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 22
# Title: Area of a Triangle (Again)

import math as m

def main():
	s1 = float(input("Side 1 (cm): "))
	s2 = float(input("Side 2 (cm): "))
	s3 = float(input("Side 3 (cm): "))

	s = (s1 + s2 + s3) / 2
	area = m.sqrt(s * (s - s1) * (s - s2) * (s - s3))

	print("Area: %.2f cm²" % area)

if __name__ == "__main__": main()