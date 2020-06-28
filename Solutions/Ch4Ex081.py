# Ch4Ex081.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 81
# Title: Compute the Hypotenuse

def calcHypo(s1, s2):
	return (((s1 ** 2) + (s2 ** 2)) ** 0.5)

def main():
	s1 = float(input("Side 1: "))
	s2 = float(input("Side 2: "))

	print("Hypotenuse: %.2f" % calcHypo(s1, s2))

if __name__ == "__main__": main()