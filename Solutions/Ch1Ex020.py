# Ch1Ex020.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 20
# Title: Ideal Gas Law

def main():
	R = 8.314
	P = float(input("Pressure (Pa): "))
	V = float(input("Volume (L): "))
	T = float(input("Temperature (∘C): "))
	n = (P * V) / (R * (T + 273.15))

	print("Amount: %.2f moles" % n)

if __name__ == "__main__": main()