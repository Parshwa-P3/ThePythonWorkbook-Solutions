# Ch1Ex015.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 15
# Title: Distance Units

def main():
	feet = float(input("Feet:   "))
	inch = feet * 12
	yard = feet * 0.333
	mile = feet * 0.000189

	print("Inches: %.2f" % (inch))
	print("Yards:  %.2f" % (yard))
	print("Miles:  %.2f" % (mile))

if __name__ == "__main__": main()