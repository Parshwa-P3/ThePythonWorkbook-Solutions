# Ch1Ex021.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 21
# Title: Area of a Triangle

def main():
	b = float(input("Base (cm): "))
	h = float(input("Height (cm): "))

	area = (b * h) / 2

	print("Area: %.2f cm²" % area)

if __name__ == "__main__": main()