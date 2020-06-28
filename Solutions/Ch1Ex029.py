# Ch1Ex029.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 29
# Title: Celcius to Fahrenheit and Kelvin

def main():
	C = float(input("In ∘C: "))

	F = (C * (9 / 5)) + 32
	K = C + 273.15

	print("In ∘F: %.2f" % F)
	print("In K: %.2f" % K)

if __name__ == "__main__": main()