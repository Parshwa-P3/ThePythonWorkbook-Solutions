# Ch1Ex004.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 4
# Title: Area of a Field

def main():
	l = float(input("Length (ft): "))
	w = float(input("Width (ft): "))

	acres = (l * w) / 43560

	print("Area: " + str(acres) + " acres")

if __name__ == "__main__": main()