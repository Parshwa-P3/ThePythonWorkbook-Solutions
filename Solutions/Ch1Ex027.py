# Ch1Ex027.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 27
# Title: Body Mass Index

def main():
	h = float(input("Height (m): "))
	w = float(input("Weight (kg): "))

	BMI = w / (h * h)

	print("BMI: %.2f" % BMI)

if __name__ == "__main__": main()