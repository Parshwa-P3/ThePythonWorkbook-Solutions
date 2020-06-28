# Ch1Ex018.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 18
# Title: Volume of a Cylinder

import math as m

def main():
	r = float(input("Radius (cm): "))
	h = float(input("Height (cm): "))
	vol = m.pi * r * r * h
	print("Volume: %.1f cm³" % (vol))

if __name__ == "__main__": main()