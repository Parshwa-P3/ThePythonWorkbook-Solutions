# Ch1Ex014.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 14
# Title: Height Units

def main():
	feet = int(input("Feet:   "))
	inch = int(input("Inches: "))
	ht = ((feet * 12) + inch) * 2.54
	print("Height: %.2f cm" % (ht))

if __name__ == "__main__": main()